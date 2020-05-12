# openebs-self-installation-check

---
tcid: TCID-DIR-OP-INSTALL-OPENEBS
name: "Install OpenEBS on user Cluster"

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
    <td> Install OpenEBS on user Cluster </td>
    <td> GKE </td>
  </tr>
</table>

## Prerequisites

- Along with k8s, Litmus should be installed in the cluster.
- Every component of DOP cluster should be healthy and running.
- Ensure that the `openebs-installation-check` resource is available in the cluster.

## Entry Criteria

- Kubernetes nodes are up and running with no openebs installed in DOP cluster .

## Exit Criteria

- Kubernetes nodes are up and running with openebs installed in DOP cluster. 

## Details

- **_Labeling the Nodes_**: Nodes are labeled for the control and data components.
  - `GET` request to the nodes on success -
  - `POST` request for the change in labels according to the condition - On which node you want to place the data components and on which node you want to place the control plan components.
- **_Generating the request for openebs installation:_**
  - A request is generated for openebs installation
  - `POST` request for openebs installation:
  - The `GET`  Respond from the previous step (in JSON format) is sent as Request to the for the installation. 

- _**Check for each GET and POST Request and Respond**_
  - There can be different ways to check the `GET` and `POST` requests - one with the status code verification 
  - Adding a status test for the previous action 
  - Adding a task for testing the expected change after each request and response.

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
