#!/bin/bash

## Run common health check tests

# Specify test name
test_name=consul-health-check
echo $test_name

sed -e 's/generateName: app-check/generateName: consul-health-check/g' \
-e 's/app: app-litmus/app: consul-health-check-litmus/g' \
-e 's/value: test-name/value: consul-health-check/g' \
-e 's/value: default /value: default/g' \
-e 's/value: pod-name/value: consul/g' oep/litmus/director/common-checks/run_litmus_test.yml \
> oep/litmus/director/common-checks/consul_run_litmus_test.yml

cat oep/litmus/director/common-checks/consul_run_litmus_test.yml

# Run common health check litmus job
kubectl create -f oep/litmus/director/common-checks/consul_run_litmus_test.yml

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
commonCheck=$(kubectl get litmusresult ${test_name} --no-headers -o custom-columns=:spec.testStatus.result)
echo $commonCheck

## Run consul specific tests

# Specify test name
test_name=consul-check
echo $test_name

# Run consul specific tests limtus job
kubectl create -f oep/litmus/director/consul/run_litmus_test.yml

sleep 2;

# Get consul check job's pod name
litmus_pod=$(kubectl get po -n litmus | grep $test_name  | awk {'print $1'} | tail -n 1)
echo $litmus_pod

# Check consul check job status
job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
while [[ "$job_status" != "Completed" ]]
do 
    job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
    sleep 6
done

# Print consul check job logs
kubectl logs -f $litmus_pod -n litmus

# Check consul check job result
consulCheck=$(kubectl get litmusresult ${test_name} --no-headers -o custom-columns=:spec.testStatus.result)
echo $consulCheck

if [ "$commonCheck" = Pass ] && [ "$consulCheck" = Pass ]; then 
testResult=Pass
else
testResult=Fail 
fi

# Flush test result in result.txt
echo "$test_name: $testResult" >> result.txt;