# openebs-self-installation-check

---
tcid: iuoi02
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

#### Sample run_litmus_test.yml

```
apiVersion: batch/v1
kind: Job
metadata:
  generateName: <test-name>-
  namespace: litmus
spec:
  template:
    metadata:
      name: litmus
      labels:
        app: <test-name>
    spec:
      serviceAccountName: litmus
      restartPolicy: Never
      volumes:
      - name: secret-volume
        secret:
          secretName: director-user-pass
      containers:
      - name: ansibletest
        image: mayadataio/dop-validator:ci
        imagePullPolicy: Always
        volumeMounts:
        - name: secret-volume
          readOnly: true
          mountPath: "/etc/secret-volume"
        env:
          
          ## Take url from configmap config
          - name: DIRECTOR_IP
            valueFrom:
              configMapKeyRef:
                name: config
                key: url

          ## Take cluster_id from configmap clusterid
          - name: CLUSTER_ID    
            valueFrom:
              configMapKeyRef:
                name: clusterid
                key: cluster_id

          ## Takes group_id from configmap groupid
          - name: GROUP_ID
            valueFrom:
              configMapKeyRef:
                name: groupid
                key: group_id

          ## It should be 1ot1 Mandatory
          - name: TEMPLATE_ID
            value: '1ot1'

          ## Namespace where openebs is installed
          ## By default in basic mode it is openebs
          - name: NAMESPACE
            value: ''

          ## Enter the default directory - It can be /var/openebs
          - name: DEFAULT_DIRECTORY
            value: ''

          ##Enter docker registry
          - name: DOCKER_REGISTRY
            value: ''

          ## Enter include device filter
          - name: INCLUDE_DEVICE_FILTERS
            value: ''

          ## Enter exclude device filter  
          - name: EXCLUDE_DEVICE_FILTER
            value: ''

          ## Enter CPU resource limit
          - name: CPU_RESOURCE_LIMIT
            value: ''

          ## Enter Memory resource limit
          - name: MEMORY_RESOURCE_LIMIT
            value: ''
          
          ## It will have values basic/advance
          ## Note: For basic installation, only template value should be provided
          ## For adding any additional value - change the installation mode to advance
          - name: INSTALLATION_MODE
            value: 'basic'

          - name: ANSIBLE_STDOUT_CALLBACK
            value: 'default'  

        command: ["/bin/bash"]
        args: ["-c", "ansible-playbook ./litmus/director/<test-path>/test.yml -i /etc/ansible/hosts -v; exit 0"]
        
```

### Watch Test progress

- View the test progress  

  `watch -n 1 kubectl logs -f pods -n <namespace>`

### Check Test Result

- Check whether the test is Pass or Fail using the following command
 
  `watch -n 1 kubectl logs -f pods -n <namespace>`

- Check the Pass and Fail value at the end of test logs.
- The pod will be in the `completed` state.
