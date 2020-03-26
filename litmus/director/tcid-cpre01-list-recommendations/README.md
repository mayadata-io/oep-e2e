# List the capacity recommendations

<b>tcid:</b> cpre01 <br>
<b>name:</b> "List the capacity recommendations"<br>


## Experiment Metadata

<table>
  <tr>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> Cstor Pool Recommendation </td>
    <td> List the capacity recommendations </td>
    <td> GKE </td>
  </tr>
</table>

## Prerequisites

- Along with k8s, Litmus should be installed in the cluster.
- Every component of DOP cluster should be healthy and running.
- Ensure that the `openebs data plane and control plane components` are available in the cluster.


## Steps Performed in the test

- Check whether OpenEBS is installed in the cluster or not.

- Also check the status of all the `Data-Plane` and `Control-Plane` components they should be in `running` state.

- First get the recommendation details by GET request on  `url: "{{ director_url }}/v3/groups/{{ group_id }}/recommendations"`

- Now you will get the `recommendation_id `

- After this, by the help of this recommendation_id POST request on  `url :'{{ director_url }}/v3/groups/{{ group_id }}/{{ recommendation_id }}/?action=getcapacityrecommendation'`  by this POST request you will get list of capacity recommendations

- BODY OF REQUEST

    `'{"clusterId":"{{ cluster_id }}", "raidGroupConfig":{"groupDeviceCount":1, "type":"stripe"}}'`

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