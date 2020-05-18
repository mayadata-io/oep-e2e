# openebs-data-plane-test

<b>tcid:</b> iuoi04 <br>
<b>name:</b> "Install OpenEBS Dataplane{NDM DS} components on specific set of nodes"<br>
<b>sidebar_label:</b> openebs-installation-test-litmus


## Experiment Metadata

<table>
  <tr>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> Openebs Installation </td>
    <td> Openebs Data plane Installation on specific set of nodes</td>
    <td> GKE </td>
  </tr>
</table>

## Prerequisites

- Along with k8s, Litmus should be installed in the cluster.
- Every component of DOP cluster should be healthy and running.
- Ensure that the `openebs-data-plane-test` resource is available in the cluster.

## Entry Criteria

- Kubernetes nodes are up and running with no data plane labels.

## Exit Criteria

- Kubernetes nodes are up and running with data plane labels as true. 

## Details

- In this test case, we have to install openebs on a particular node. It can be done by labeling the nodes before installing the openebs on it. So basically we will test that the labeling feature is working fine with respective of data plane components. Data plane components include  NDM daemonset.

- The tasks involved for creating the test case will be - we will labels nodes as shown in the table.

<table>
  <tr>
    <th> OpenEBS components </th>
    <th>  Node-1  </th>
    <th>  Node-2  </th>
    <th>  Node-3  </th>
  </tr>
  <tr>
    <td> <b>Data plane components</b> </td>
    <td> True  </td>
    <td> False </td>
    <td> False </td>
  </tr>
  <tr>
    <td> <b>Control plane components</b> </td>
    <td> False </td>
    <td> True  </td>
    <td> True  </td>
  </tr>
</table>

## Integrations

- This test can be performed on GKE cluster where the openebs is already installed.
- The desired specification for installing openebs can be done by passing the values from `run_litmus_tes.yml`. And then we have to select the `installation mode` which can have two different modes `basic` and `advance`. For installing openebs with default values use `basic` mode and for installing openebs with the desired value it will be `advance`.

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
