# List cstor pool recommendations without NDM

<b>tcid:</b> TCID-DIR-OP-CSP-REC-LIST-NO-NDM <br>
<b>name:</b> "List cstor pool recommendations without NDM"<br>


## Experiment Metadata

<table>
  <tr>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> Cstor Pool Recommendation </td>
    <td> List cstor pool recommendations without NDM </td>
    <td> GKE </td>
  </tr>
</table>

## Prerequisites

- Cluster create setup should be done
- DOP should be installed
- NDM should not be running

## Details

- Director version 1.9 onwards
- Negative test case

## Steps Performed in the test

- Invoke API to list recommendations
- Invoke API to get capacity based recommendations
- Invoke API to get device based recommendations

### Expected output

- Director should list the supported recommendations without error
- Director should list the capacity based recommendations without error
- Director should list the device based recommendations without error

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