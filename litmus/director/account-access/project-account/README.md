# teaming-project-account-resources-check

---

tcid: TRPA01

name: Check Project Account access resources
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
    <td> Project Account Access Check </td>
    <td> Check Project Account access resources </td>
    <td> GKE </td>
  </tr>
</table>

## Prerequisites

- Along with k8s, Litmus should be installed in the cluster.
- Every component of DOP cluster should be healthy and running.
- User cluster must be connected to the Director OnPrem.
- OpenEBS should be installed along with some application.

###  Details of TestCases

- From a ProjectAccount, fetch all clusters applications.
- From a ProjectAccount, fetch all clusters storage pools. 
- Check if cluster pool pods is same as ProjectAccount  pool pod resources.
- Check if cluster applications is same as ProjectAccount maya-app resources.

## Expected results

- Inside project account we should get all connected clusters resources i.e., pools, maya   applications
Note: For current since only one cluster is connected to Director OnPrem

## Entry Criteria

- Project Account should be present on Director OnPrem .

## Exit Criteria

- Project Account resources are fetched and verified on the user cluster. 

## Details

- **_Fetching account resources:_**
  - Running /api_testing/group/access.py script with account as argument i.e., ProjectAccount in this caseto fetch pool and maya resources

- **_Generating the request for openebs installation:_**
  - Verifying account fetched resources with cluster resources

## Integrations

- This test can be performed on GKE cluster where DOP is installed.

## Steps to Execute the test manually 

- Use `run_litmus_test.yml` with the your `image` (contains the image of the experiment) , `secret`(contains the userid and password), `configmaps`(contains dop url and cluster id) files and other environment variables.
- Create `run_litmus_test.yml` file in `litmus` namespace. 
- Check the test log using `kubectl logs -f <jobs-pod-name> -n <litmus>` command.

## Expected results

### Watch Test progress

- View the test progress  

  `watch -n 1 kubectl logs -f pods -n <namespace>`

### Check Test Result

- Check whether the test is Pass or Fail using the following command
 
  `watch -n 1 kubectl logs -f pods -n <namespace>`

- Check the Pass and Fail value at the end of test logs.
- The pod will be in the `completed` state.
