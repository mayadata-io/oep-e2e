#!/bin/bash

# Specify test name
test_name=cassandra-check
echo $test_name

# Run cassandra check litmus job
kubectl create -f oep-e2e/litmus/director/cassandra/run_litmus_test.yml

sleep 2;

# Get cassandra-check job's pod name
litmus_pod=$(kubectl get po -n litmus | grep $test_name  | awk {'print $1'} | tail -n 1)
echo $litmus_pod

# Check cassandra-check job's status
job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
while [[ "$job_status" != "Completed" ]]
do 
    job_status=$(kubectl get po  $litmus_pod -n litmus | awk {'print $3'} | tail -n 1)
    sleep 6
done

# Print cassandra-check job logs
kubectl logs -f $litmus_pod -n litmus

# Check cassandra-check job result
testResult=$(kubectl get litmusresult ${test_name} --no-headers -o custom-columns=:spec.testStatus.result)
echo $testResult

# Flush test result in result.txt
echo "$test_name: $testResult" >> result.txt;