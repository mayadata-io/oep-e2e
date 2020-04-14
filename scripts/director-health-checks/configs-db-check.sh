#!/bin/bash

## Run common health check tests

# Specify test name
test_name=configs-db-health-check
echo $test_name

sed -e 's/generateName: app-check/generateName: configs-db-health-check/g' \
-e 's/app: app-litmus/app: configs-db-health-check-litmus/g' \
-e 's/value: test-name/value: configs-db-health-check/g' \
-e 's/value: default /value: default/g' \
-e 's/value: pod-name/value: configs-db/g' oep-e2e/litmus/director/common-checks/run_litmus_test.yml \
> oep-e2e/litmus/director/common-checks/configs_db_run_litmus_test.yml

cat oep-e2e/litmus/director/common-checks/configs_db_run_litmus_test.yml

# Run common health check litmus job
kubectl create -f oep-e2e/litmus/director/common-checks/configs_db_run_litmus_test.yml

sleep 2;

# Get common health check job's pod name
litmus_pod=$(kubectl get po -n litmus | grep $test_name  | awk {'print $1'} | tail -n 1)
echo $litmus_pod

# Check common health check job status
job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
while [[ "$job_status" != "Completed" ]]
do 
    job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
    sleep 6
done

# Print common health check job logs
kubectl logs -f $litmus_pod -n litmus

# Check common health check job result
commonCheck=$(kubectl get litmusresult $test_name --no-headers -o custom-columns=:spec.testStatus.result)
echo $commonCheck

## Run configs-db specific tests

# Specify test name
test_name=configs-db-check
echo $test_name

# Run configs-db specific tests limtus job
kubectl create -f oep-e2e/litmus/director/configs-db/run_litmus_test.yml

sleep 2;

# Get configs-db check job's pod name
litmus_pod=$(kubectl get po -n litmus | grep $test_name  | awk {'print $1'} | tail -n 1)
echo $litmus_pod

# Check configs-db check job status
job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
while [[ "$job_status" != "Completed" ]]
do 
    job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
    sleep 6
done

# Print configs-db check job logs
kubectl logs -f $litmus_pod -n litmus

# Check configs-db check job result
confisdbCheck=$(kubectl get litmusresult $test_name --no-headers -o custom-columns=:spec.testStatus.result)
echo $confisdbCheck

if [ "$commonCheck" = Pass ] && [ "$confisdbCheck" = Pass ]; then 
testResult=Pass
else
testResult=Fail 
fi

# Flush test result in result.txt
echo "$test_name: $testResult" >> result.txt;