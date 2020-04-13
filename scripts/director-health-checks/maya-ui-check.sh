#!/bin/bash

# Specify test name
test_name=maya-ui-check
echo $test_name

# Run maya-ui check litmus job
kubectl create -f oep/litmus/director/maya-ui/run_litmus_test.yml

sleep 2;

# Get maya-ui-check job's pod name
litmus_pod=$(kubectl get po -n litmus | grep $test_name  | awk {'print $1'} | tail -n 1)
echo $litmus_pod

# Check maya-ui-check job's status
job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
while [[ "$job_status" != "Completed" ]]
do 
    job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
    sleep 6
done

# Print maya-ui-check job logs
kubectl logs -f $litmus_pod -n litmus

# Check maya-ui-check job result
testResult=$(kubectl get litmusresult $test_name --no-headers -o custom-columns=:spec.testStatus.result)
echo $testResult

# Flush test result in result.txt
echo "$test_name: $testResult" >> result.txt;