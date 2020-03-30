# teaming-cluster-account-resources-check

---
tcid: 
name: "Check Cluster Account access resources"
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

## Entry Criteria

- Cluster Account should be present on Director OnPrem .

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

#### Sample run_litmus_test.yml

```
---
apiVersion: batch/v1
kind: Job
metadata:
  generateName: cluster-account-resources-check
  namespace: litmus
spec:
  template:
    metadata:
      name: litmus
      labels:
        app: cluster-account-resources-check-litmus
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
        args: ["-c", "ansible-playbook ./litmus/director/account-access/cluster-account/test.yaml -i /etc/ansible/hosts -v; exit 0"]
      imagePullSecrets:
      - name: oep-secret
  
```

### Details of TestCases

- Inside a ClusterAccount, will get all cluster specific applications.
- Inside a ClusterAccount, will get all cluster specific storage pools.
- Check if cluster pool pods is same as ClusterAccount pool pod resources.
- Check if cluster applications is same as ClusterAccount maya-app resources.

## Expected results

Logs of testcases: 
```
PLAY [localhost] ***************************************************************

TASK [Gathering Facts] *********************************************************
ok: [127.0.0.1]

TASK [include_tasks] ***********************************************************
included: /ansible-utils/create_testname.yml for 127.0.0.1

TASK [Record test instance/run ID] *********************************************
skipping: [127.0.0.1] => {"changed": false, "skip_reason": "Conditional result was False"}

TASK [Construct testname appended with runID] **********************************
skipping: [127.0.0.1] => {"changed": false, "skip_reason": "Conditional result was False"}

TASK [include_tasks] ***********************************************************
included: /ansible-utils/update_litmus_result_resource.yml for 127.0.0.1

TASK [Generate the litmus result CR to reflect SOT (Start of Test)] ************
changed: [127.0.0.1] => {"changed": true, "checksum": "9b17de1263078377b5457817149c992997beb218", "dest": "./litmus-result.yaml", "gid": 0, "group": "root", "md5sum": "f159984f5d10c9b26f6a1a76cb5b848d", "mode": "0644", "owner": "root", "size": 422, "src": "/root/.ansible/tmp/ansible-tmp-1584607977.2310188-188687646030618/source", "state": "file", "uid": 0}

TASK [Analyze the cr yaml] *****************************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "cat litmus-result.yaml", "delta": "0:00:00.003244", "end": "2020-03-19 08:52:58.264955", "rc": 0, "start": "2020-03-19 08:52:58.261711", "stderr": "", "stderr_lines": [], "stdout": "---\napiVersion: litmus.io/v1alpha1\nkind: LitmusResult\nmetadata:\n\n  # name of the litmus testcase\n  name: account-resources-check \nspec:\n\n  # holds information on the testcase\n  testMetadata:\n    app:  \n    chaostype:  \n\n  # holds the state of testcase,  manually updated by json merge patch\n  # result is the useful value today, but anticipate phase use in future \n  testStatus: \n    phase: in-progress  \n    result: none ", "stdout_lines": ["---", "apiVersion: litmus.io/v1alpha1", "kind: LitmusResult", "metadata:", "", "  # name of the litmus testcase", "  name: account-resources-check ", "spec:", "", "  # holds information on the testcase", "  testMetadata:", "    app:  ", "    chaostype:  ", "", "  # holds the state of testcase,  manually updated by json merge patch", "  # result is the useful value today, but anticipate phase use in future ", "  testStatus: ", "    phase: in-progress  ", "    result: none "]}

TASK [Apply the litmus result CR] **********************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "kubectl apply -f litmus-result.yaml", "delta": "0:00:00.533722", "end": "2020-03-19 08:52:59.035260", "failed_when_result": false, "rc": 0, "start": "2020-03-19 08:52:58.501538", "stderr": "", "stderr_lines": [], "stdout": "litmusresult.litmus.io/account-resources-check configured", "stdout_lines": ["litmusresult.litmus.io/account-resources-check configured"]}

TASK [Generate the litmus result CR to reflect EOT (End of Test)] **************
skipping: [127.0.0.1] => {"changed": false, "skip_reason": "Conditional result was False"}

TASK [Analyze the cr yaml] *****************************************************
skipping: [127.0.0.1] => {"changed": false, "skip_reason": "Conditional result was False"}

TASK [Apply the litmus result CR] **********************************************
skipping: [127.0.0.1] => {"changed": false, "skip_reason": "Conditional result was False"}

TASK [set_fact] ****************************************************************
ok: [127.0.0.1] => {"ansible_facts": {"director_url": "http://34.74.102.61:30380"}, "changed": false}

TASK [Get username] ************************************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "cat /etc/secret-volume/username", "delta": "0:00:00.003299", "end": "2020-03-19 08:52:59.404193", "rc": 0, "start": "2020-03-19 08:52:59.400894", "stderr": "", "stderr_lines": [], "stdout": "866936543B7C8468E386", "stdout_lines": ["866936543B7C8468E386"]}

TASK [Get password] ************************************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "cat /etc/secret-volume/password", "delta": "0:00:00.003665", "end": "2020-03-19 08:52:59.664595", "rc": 0, "start": "2020-03-19 08:52:59.660930", "stderr": "", "stderr_lines": [], "stdout": "v2HDWEk5SwwoRDucQHFdDcmtK4sbppY6S9P2nv9E", "stdout_lines": ["v2HDWEk5SwwoRDucQHFdDcmtK4sbppY6S9P2nv9E"]}

TASK [Fetch pool pods from cluster] ********************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "kubectl get pods -n openebs | grep cstor | awk '{print $1}'", "delta": "0:00:00.074044", "end": "2020-03-19 08:52:59.949423", "rc": 0, "start": "2020-03-19 08:52:59.875379", "stderr": "", "stderr_lines": [], "stdout": "cstor-sparse-pool-7chc-58466f479b-qnp4v\ncstor-sparse-pool-8hej-8cf4456f6-6ltc2\ncstor-sparse-pool-cs7n-7d884698ff-r9nps", "stdout_lines": ["cstor-sparse-pool-7chc-58466f479b-qnp4v", "cstor-sparse-pool-8hej-8cf4456f6-6ltc2", "cstor-sparse-pool-cs7n-7d884698ff-r9nps"]}

TASK [Get cluster pool resources for ClusterAccount] ***************************
changed: [127.0.0.1] => {"changed": true, "cmd": "python3 /api_testing/group/access.py --username 866936543B7C8468E386 --password v2HDWEk5SwwoRDucQHFdDcmtK4sbppY6S9P2nv9E --account ClusterAccount --url http://34.74.102.61:30380 --resource pool", "delta": "0:00:00.184224", "end": "2020-03-19 08:53:00.343530", "rc": 0, "start": "2020-03-19 08:53:00.159306", "stderr": "", "stderr_lines": [], "stdout": "cstor-sparse-pool-7chc-58466f479b-qnp4v\ncstor-sparse-pool-8hej-8cf4456f6-6ltc2\ncstor-sparse-pool-cs7n-7d884698ff-r9nps", "stdout_lines": ["cstor-sparse-pool-7chc-58466f479b-qnp4v", "cstor-sparse-pool-8hej-8cf4456f6-6ltc2", "cstor-sparse-pool-cs7n-7d884698ff-r9nps"]}

TASK [Check if cluster pool pods is same as Cluster Account pool pod resources] ***
changed: [127.0.0.1] => {"changed": true, "cmd": "echo \"pool pods list found on the cluster is same as director cluster account maya app resources\"", "delta": "0:00:00.003073", "end": "2020-03-19 08:53:00.592702", "failed_when_result": false, "rc": 0, "start": "2020-03-19 08:53:00.589629", "stderr": "", "stderr_lines": [], "stdout": "pool pods list found on the cluster is same as director cluster account maya app resources", "stdout_lines": ["pool pods list found on the cluster is same as director cluster account maya app resources"]}

TASK [Get cluster application resources for ClusterAccount] ********************
changed: [127.0.0.1] => {"changed": true, "cmd": "python3 /api_testing/group/access.py --username 866936543B7C8468E386 --password v2HDWEk5SwwoRDucQHFdDcmtK4sbppY6S9P2nv9E --account ClusterAccount --url http://34.74.102.61:30380 --resource maya-app", "delta": "0:00:00.161250", "end": "2020-03-19 08:53:00.989918", "rc": 0, "start": "2020-03-19 08:53:00.828668", "stderr": "", "stderr_lines": [], "stdout": "mongo", "stdout_lines": ["mongo"]}

TASK [Fetch statefulset applications from cluster] *****************************
changed: [127.0.0.1] => (item=app-mongo-ns) => {"ansible_loop_var": "item", "attempts": 1, "changed": true, "cmd": "kubectl get sts -n app-mongo-ns --no-headers | awk '{print $1}'", "delta": "0:00:00.072718", "end": "2020-03-19 08:53:01.283224", "item": "app-mongo-ns", "rc": 0, "start": "2020-03-19 08:53:01.210506", "stderr": "", "stderr_lines": [], "stdout": "mongo", "stdout_lines": ["mongo"]}

TASK [Fetch deployment applications from cluster] ******************************
skipping: [127.0.0.1] => (item=)  => {"ansible_loop_var": "item", "changed": false, "item": "", "skip_reason": "Conditional result was False"}

TASK [set_fact] ****************************************************************
ok: [127.0.0.1] => {"ansible_facts": {"flag": "Pass"}, "changed": false}

TASK [include_tasks] ***********************************************************
included: /ansible-utils/update_litmus_result_resource.yml for 127.0.0.1

TASK [Generate the litmus result CR to reflect SOT (Start of Test)] ************
skipping: [127.0.0.1] => {"changed": false, "skip_reason": "Conditional result was False"}

TASK [Analyze the cr yaml] *****************************************************
skipping: [127.0.0.1] => {"changed": false, "skip_reason": "Conditional result was False"}

TASK [Apply the litmus result CR] **********************************************
skipping: [127.0.0.1] => {"changed": false, "skip_reason": "Conditional result was False"}

TASK [Generate the litmus result CR to reflect EOT (End of Test)] **************
changed: [127.0.0.1] => {"changed": true, "checksum": "e3729e5bd0348710d6a1c62702b2a4cf2a5652be", "dest": "./litmus-result.yaml", "gid": 0, "group": "root", "md5sum": "1d0e7871f83e12f56f24a4c00fc224e3", "mode": "0644", "owner": "root", "size": 420, "src": "/root/.ansible/tmp/ansible-tmp-1584607981.6297836-117926121854716/source", "state": "file", "uid": 0}

TASK [Analyze the cr yaml] *****************************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "cat litmus-result.yaml", "delta": "0:00:00.003179", "end": "2020-03-19 08:53:02.182698", "rc": 0, "start": "2020-03-19 08:53:02.179519", "stderr": "", "stderr_lines": [], "stdout": "---\napiVersion: litmus.io/v1alpha1\nkind: LitmusResult\nmetadata:\n\n  # name of the litmus testcase\n  name: account-resources-check \nspec:\n\n  # holds information on the testcase\n  testMetadata:\n    app:  \n    chaostype:  \n\n  # holds the state of testcase,  manually updated by json merge patch\n  # result is the useful value today, but anticipate phase use in future \n  testStatus: \n    phase: completed  \n    result: Pass ", "stdout_lines": ["---", "apiVersion: litmus.io/v1alpha1", "kind: LitmusResult", "metadata:", "", "  # name of the litmus testcase", "  name: account-resources-check ", "spec:", "", "  # holds information on the testcase", "  testMetadata:", "    app:  ", "    chaostype:  ", "", "  # holds the state of testcase,  manually updated by json merge patch", "  # result is the useful value today, but anticipate phase use in future ", "  testStatus: ", "    phase: completed  ", "    result: Pass "]}

TASK [Apply the litmus result CR] **********************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "kubectl apply -f litmus-result.yaml", "delta": "0:00:00.264660", "end": "2020-03-19 08:53:02.660446", "failed_when_result": false, "rc": 0, "start": "2020-03-19 08:53:02.395786", "stderr": "", "stderr_lines": [], "stdout": "litmusresult.litmus.io/account-resources-check configured", "stdout_lines": ["litmusresult.litmus.io/account-resources-check configured"]}

PLAY RECAP *********************************************************************
127.0.0.1                  : ok=19   changed=13   unreachable=0    failed=0    skipped=9    rescued=0    ignored=0   
```

### Watch Test progress

- View the test progress  

  `watch -n 1 kubectl logs -f pods -n <namespace>`

### Check Test Result

- Check whether the test is Pass or Fail using the following command
 
  `watch -n 1 kubectl logs -f pods -n <namespace>`

- Check the Pass and Fail value at the end of test logs.
- The pod will be in the `completed` state.
