#!/bin/bash

# Run maya-io-server-check litmus job
kubectl create -f oep-e2e/litmus/director/maya-io-server/run_litmus_test.yml

test_name=maya-io-server-check
echo $test_name

sleep 2;

litmus_pod=$(kubectl get po -n litmus | grep $test_name  | awk {'print $1'} | tail -n 1)
echo $litmus_pod

# Check maya-io-server-check job status
job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
while [[ "$job_status" != "Completed" ]]
do 
    job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
    sleep 6
done

# Print maya-io-server-check job logs
kubectl logs -f $litmus_pod -n litmus

# Check maya-io-server-check job results
testResult=$(kubectl get litmusresult ${test_name} --no-headers -o custom-columns=:spec.testStatus.result)

echo $testResult 
echo "$test_name: $testResult" >> result.txt;