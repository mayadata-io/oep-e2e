# Verify raidz cstor pool cluster after node reboot

<b>tcid:</b> TCID-DIR-OP-CSTOR-POOL-RAIDZ-RECOMMEND-REBOOT-NODE <br>
<b>name:</b> "Verify raidz cstor pool cluster after node reboot"<br>


## Experiment Metadata

<table>
  <tr>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> Cstor Pool Recommendation </td>
    <td> Verify raidz cstor pool cluster after node reboot </td>
    <td> GKE </td>
  </tr>
</table>

## Prerequisites

- Along with k8s, Litmus should be installed in the cluster.
- Every component of DOP cluster should be healthy and running.
- Ensure that the `openebs data plane and control plane components` are available in the cluster.

## Details

- Director version 1.9 onwards
- Negative test case

## Steps Performed in the test

- Invoke API to list recommendations
- Invoke API to get capacity based recommendations
- Invoke API to get device based recommendations
- Invoke API to get raidz based cstor pool recommendations
- Invoke API to create raidz cstor pool cluster
- Reboot node and then verify the status of pools

### Expected output

- Director should be able to create raidz cstor pool cluster

## Integrations

- This test can be performed on GKE cluster where the openebs is already installed and the version of openebs should be less the 1.7.0.

## Steps to Execute the test manually 

- Use `run_litmus_test.yml` with the your `image` (contains the image of the experiment) , `secret`(contains the userid and password), `configmaps`(contains dop url and cluster id) files and other environment variables.
- Create `run_litmus_test.yml` file in `litmus` namespace. 
- Check the test log using `kubectl logs -f <jobs-pod-name> -n <litmus>` command.


### Watch Test progress

- View the test progress  

  `watch -n 1 kubectl logs -f pods -n <namespace>`

### Check Test Result

- Check whether the test is Pass or Fail using the following command

  `watch -n 1 kubectl logs -f pods -n <namespace>`

- Check the Pass and Fail value at the end of test logs.
- The pod will be in the `completed` state.