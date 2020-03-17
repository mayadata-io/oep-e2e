# Upgrade the application with 3 replicas when all pool pod are running

<b>tcid:</b> iuod24 <br>
<b>name:</b> "Upgrade the application with 3 replicas when all pool pod are running" <br>


## Experiment Metadata

<table>
  <tr>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> Install and Upgrade of OpenEBS </td>
    <td> Upgrade the application with 3 replicas when all pool pod are running </td>
    <td> GKE </td>
  </tr>
</table>

## Prerequisites

- Along with k8s, Litmus should be installed in the cluster.
- Every component of DOP cluster should be healthy and running.
- Ensure that the `openebs data plane and control plane components` are available in the cluster.


## Details
- In this test case we have to upgrade only the `Data Plane` components using DOP when one pool pod is not in running state.


- `Data Plane` components should not get upgraded because one pool pod is not in running state.

## Steps Performed in the test

- Check whether OpenEBS is installed in the cluster or not.

- Also check the status of all the `Data-Plane` and `Control-Plane` components they should be in `running` state.

- Version of OpenEBS should be less then 1.7.0 .

- First upgrade `Control-Plane` components, check whether all the components are in running state or not.

- After upgrading `Control-Plane` components upgrade `Data-Plane` components .

- .


## Integrations

- This test can be performed on GKE cluster where the openebs is already installed and the version of openebs should be less the 1.7.0.

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
          
          - name: ANSIBLE_STDOUT_CALLBACK
            value: 'default'  
        command: ["/bin/bash"]
        args: ["-c", "ansible-playbook ./litmus/director/<test-path>/test.yml -i /etc/ansible/hosts -v; exit 0"]
        
      imagePullSecrets:
        - name: oep-secret 
```

### Watch Test progress

- View the test progress  

  `watch -n 1 kubectl logs -f pods -n <namespace>`

### Check Test Result

- Check whether the test is Pass or Fail using the following command

  `watch -n 1 kubectl logs -f pods -n <namespace>`

- Check the Pass and Fail value at the end of test logs.
- The pod will be in the `completed` state.