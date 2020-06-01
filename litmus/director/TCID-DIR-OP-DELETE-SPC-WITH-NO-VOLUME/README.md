# Delete SPC via director which has no volume

<b>tcid:</b> TCID-DIR-OP-DELETE-SPC-WITH-NO-VOLUME <br>
<b>name:</b> "Delete SPC via director which has no volume"<br>


## Experiment Metadata

<table>
  <tr>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> Cstor Pool Recommendation </td>
    <td> Delete SPC via director which has no volume </td>
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

- Delete SPC via director which has no volume

## Steps Performed in the test

- Check whether OpenEBS is installed in the cluster or not.

- Also check the status of all the `Data-Plane` and `Control-Plane` components they should be in `running` state.

- Create SPC using yaml.

- Invoke API to delete SPC using director

- Now wait until CStorPoolOpetation's state become success.

- After this delete the SPC using director.


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