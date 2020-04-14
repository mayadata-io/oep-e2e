#!/bin/bash

## Run common health check

# Specify test name
test_name=od-elasticsearch-health-check
echo $test_name

sed -e 's/generateName: app-check/generateName: od-elasticsearch-health-check/g' \
-e 's/app: app-litmus/app: od-elasticsearch-health-check-litmus/g' \
-e 's/value: test-name/value: od-elasticsearch-health-check/g' \
-e 's/value: default /value: default/g' \
-e 's/value: pod-name/value: od-elasticsearch/g' oep-e2e/litmus/director/common-checks/run_litmus_test.yml \
> oep-e2e/litmus/director/common-checks/es_run_litmus_test.yml

cat oep-e2e/litmus/director/common-checks/es_run_litmus_test.yml

# Run common health check litmus job
kubectl create -f oep-e2e/litmus/director/common-checks/es_run_litmus_test.yml

sleep 2;

# Check common health check job status
litmus_pod=$(kubectl get po -n litmus | grep $test_name  | awk {'print $1'} | tail -n 1)
echo $litmus_pod
job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
while [[ "$job_status" != "Completed" ]]
do 
    job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
    sleep 6
done

# Print common health check job logs
kubectl logs -f $litmus_pod -n litmus

# Check common health check job result
commonCheck=$(kubectl get litmusresult ${test_name} --no-headers -o custom-columns=:spec.testStatus.result)
echo $commonCheck;

## Run od-elasticsearch specific limtus job

# Specify test name
test_name=od-elasticsearch-check
echo $test_name

# Run od-elasticsearch specific tests limtus job
kubectl create -f oep-e2e/litmus/director/od-elasticsearch/run_litmus_test.yml

sleep 2;

# Get od-elasticsearch check job's pod name
litmus_pod=$(kubectl get po -n litmus | grep $test_name  | awk {'print $1'} | tail -n 1)
echo $litmus_pod

# Check od-elasticsearch check job status
job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
while [[ "$job_status" != "Completed" ]]
do 
    job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
    sleep 6
done

# Print od-elasticsearch check job logs
kubectl logs -f $litmus_pod -n litmus

# Check od-elasticsearch check job result
elasticsearchCheck=$(kubectl get litmusresult ${test_name} --no-headers -o custom-columns=:spec.testStatus.result)
echo $elasticsearchCheck

if [ "$commonCheck" = Pass ] && [ "$elasticsearchCheck" = Pass ]; then 
testResult=Pass
else
testResult=Fail 
fi

# Flush test result in result.txt
echo "$test_name: $testResult" >> result.txt;