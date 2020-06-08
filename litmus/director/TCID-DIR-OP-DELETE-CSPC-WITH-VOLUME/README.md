# Delete CSPC created via director which has volume

<b>tcid:</b> TCID-DIR-OP-DELETE-CSPC-WITH-VOLUME <br>
<b>name:</b> "Delete CSPC created via director which has volume"<br>


## Experiment Metadata

<table>
  <tr>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> Cstor Pool Recommendation </td>
    <td> Delete CSPC created via director which has volume </td>
    <td> GKE </td>
  </tr>
</table>

## Prerequisites

- Along with k8s, Litmus should be installed in the cluster.
- Every component of DOP cluster should be healthy and running.
- Ensure that the `openebs data plane and control plane components` are available in the cluster.

## Details

- This test cases is to create cstor pool using recommendations.

### Expected output

- It should not able to delete CSPC 

## Steps Performed in the test

- Check whether OpenEBS is installed in the cluster or not.

- Also check the status of all the `Data-Plane` and `Control-Plane` components they should be in `running` state.

- First get the recommendation details by GET request on  `url: "{{ director_url }}/v3/groups/{{ group_id }}/recommendations"`

- Now you will get the `recommendation_id `

- After this, by the help of this recommendation_id POST request on  `url :'{{ director_url }}/v3/groups/{{ group_id }}/{{ recommendation_id }}/?action=getdevicerecommendation'`  by this POST request you will get list of device recommendations

- BODY OF REQUEST

    `'{"clusterId":"{{ cluster_id }}", "deviceGroupName": null,"poolCapacity":"1G","poolName":null, "raidGroupConfig":{"groupDeviceCount":1, "type":"stripe"}}'`

- After getting device recommendation fetch the json data and POST request on ` {director-url}/v3/groups/1a{group-id}/recommendations/cstorpooloperations`

- At last give POST request on `{director-url}/v3/groups/1a{group-id}/cstorpooloperations/1cpo{cstorpooloperation-id}/?action=execute` to execute CStorPoolOpetation

- Now wait until CStorPoolOpetation's state become success.

- After this delete the cspc using director.


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