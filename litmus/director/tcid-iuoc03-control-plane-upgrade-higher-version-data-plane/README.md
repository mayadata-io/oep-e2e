# Upgrade of control plane(1.6) which is lower version of Data plane (1.7)

---
tcid: iuoc03
name: "Upgrade of control plane(1.6) which is lower version of Data plane (1.7)"

---
------

## Experiment Metadata

<table>
  <tr>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> Openebs Installation </td>
    <td> "Upgrade of control plane(1.6) which is lower version of Data plane (1.7)" </td>
    <td> GKE </td>
  </tr>
</table>

## Prerequisites

- Along with k8s, Litmus should be installed in the cluster.
- Every component of DOP cluster should be healthy and running.
- Ensure that the openebs is already installed in the cluster.

## Details

- Upgrade of control plane(1.6) which is lower version of Data plane (1.7)

### Expected output

- Upgrade of Control-Plane components should not proceed because the Data-Plane components are of lower version. 

## Steps Performed in the test

- Check whether OpenEBS is installed in the cluster or not.

- Also check the status of all the `Data-Plane` and `Control-Plane` components they should be in `running` state.

- Data Plane components should be lower version and Control Plane components should be upgraded to higher version. 

- Get active openebs record from  `v3/groups/{gropu_id}/cluster/{cluster_id}/openebs/{openebs_id}`

- After that trigger action `upgradecontrolplane`. Once we triggered the action with the target version as input. It will give error becaue the Data-Plane components are of lower version.


## Integrations

- This test can be performed on GKE cluster where DOP is installed.
- The desired specification for installing openebs in DOP cluster can be done by passing the values from `run_litmus_tes.yml`. And then we have to select the `installation mode` which can have two different modes `basic` and `advance`. For installing openebs with default values use `basic` mode and for installing openebs with the desired value it will be `advance`.

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