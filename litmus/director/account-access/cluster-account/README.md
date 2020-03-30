# teaming-cluster-account-resources-check

---

tcid: TRCA01

name: Check Cluster Account access resources
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
    <td> Cluster Account Access Check </td>
    <td> Check Cluster Account access resources </td>
    <td> GKE </td>
  </tr>
</table>

## Prerequisites

- Along with k8s, Litmus should be installed in the cluster.
- Every component of DOP cluster should be healthy and running.
- User cluster must be connected to the Director OnPrem.
- OpenEBS should be installed along with some application.

### Details of TestCases

- From a ClusterAccount, fetch cluster specific applications.
- From a ClusterAccount, fetch cluster specific storage pools.
- Check if cluster pool pods is same as ClusterAccount pool pod resources.
- Check if cluster applications is same as ClusterAccount maya-app resources.

## Expected results

- Inside cluster account we should get all the cluster specific resources i.e., pools, maya     applications

## Entry Criteria

- Cluster Account should be present on Director OnPrem.

## Exit Criteria

- Cluster Account resources are fetched and verified on the user cluster. 

## Details

- **_Fetching account resources:_**
  - Running /api_testing/group/access.py script with account as argument i.e., ClusterAccount in this caseto fetch pool and maya resources

- **_Generating the request for openebs installation:_**
  - Verifying account fetched resources with cluster resources

## Integrations

- This test can be performed on GKE cluster where DOP is installed.

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
