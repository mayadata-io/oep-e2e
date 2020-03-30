# teaming-project-account-resources-check

---
tcid: 
name: "Check Project Account access resources"
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

## Entry Criteria

- Project Account should be present on Director OnPrem .

## Exit Criteria

- Project Account resources are fetched and verified on the user cluster. 

## Details

- **_Fetching account resources
  - Running /api_testing/group/access.py script with account as argument i.e., ProjectAccount in this caseto fetch pool and maya resources

- **_Generating the request for openebs installation:_**
  - Verifying account fetched resources with cluster resources

## Integrations

- This test can be performed on GKE cluster where DOP is installed.

## Steps to Execute the test manually 

- Use `run_litmus_test.yml` with the your `image` (contains the image of the experiment) , `secret`(contains the userid and password), `configmaps`(contains dop url and cluster id) files and other environment variables.
- Create `run_litmus_test.yml` file in `litmus` namespace. 
- Check the test log using `kubectl logs -f <jobs-pod-name> -n <litmus>` command.

#### Sample run_litmus_test.yml

```
---
apiVersion: batch/v1
kind: Job
metadata:
  generateName: project-account-resources-check
  namespace: litmus
spec:
  template:
    metadata:
      name: litmus
      labels:
        app: project-account-resources-check-litmus
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
          - name: DIRECTOR_IP
            valueFrom:
              configMapKeyRef:
                name: config
                key: url
          - name: WEB_PROTOCOL
            value: http
          - name: DIRECTOR_PORT
            value: "30380"
          - name: STS_NAMESPACE_LIST
            value: '["app-mongo-ns"]'
          - name: DEPLOYMENT_NAMESPACE_LIST
            value: ''
          - name: ANSIBLE_STDOUT_CALLBACK
            value: default  
        command: ["/bin/bash"]
        args: ["-c", "ansible-playbook ./litmus/director/account-access/project-account/test.yaml -i /etc/ansible/hosts -v; exit 0"]
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
