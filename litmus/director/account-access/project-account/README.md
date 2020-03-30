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

- **_Fetching account resources:_**
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

###  Details of TestCases

- Inside a ProjectAccount, will get all clusters applications.
- Inside a ProjectAccount, will get all clusters storage pools. 
- Check if cluster pool pods is same as ProjectAccount  pool pod resources.
- Check if cluster applications is same as ProjectAccount maya-app resources.

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
changed: [127.0.0.1] => {"changed": true, "checksum": "9a51831374f64739a451d0775e4085542a0df3b7", "dest": "./litmus-result.yaml", "gid": 0, "group": "root", "md5sum": "eab7e975decf4cd66190b0b013299775", "mode": "0644", "owner": "root", "size": 430, "src": "/root/.ansible/tmp/ansible-tmp-1584657375.2821045-166231036878860/source", "state": "file", "uid": 0}

TASK [Analyze the cr yaml] *****************************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "cat litmus-result.yaml", "delta": "0:00:00.004436", "end": "2020-03-19 22:36:16.298938", "rc": 0, "start": "2020-03-19 22:36:16.294502", "stderr": "", "stderr_lines": [], "stdout": "---\napiVersion: litmus.io/v1alpha1\nkind: LitmusResult\nmetadata:\n\n  # name of the litmus testcase\n  name: project-account-resources-check \nspec:\n\n  # holds information on the testcase\n  testMetadata:\n    app:  \n    chaostype:  \n\n  # holds the state of testcase,  manually updated by json merge patch\n  # result is the useful value today, but anticipate phase use in future \n  testStatus: \n    phase: in-progress  \n    result: none ", "stdout_lines": ["---", "apiVersion: litmus.io/v1alpha1", "kind: LitmusResult", "metadata:", "", "  # name of the litmus testcase", "  name: project-account-resources-check ", "spec:", "", "  # holds information on the testcase", "  testMetadata:", "    app:  ", "    chaostype:  ", "", "  # holds the state of testcase,  manually updated by json merge patch", "  # result is the useful value today, but anticipate phase use in future ", "  testStatus: ", "    phase: in-progress  ", "    result: none "]}

TASK [Apply the litmus result CR] **********************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "kubectl apply -f litmus-result.yaml", "delta": "0:00:00.416200", "end": "2020-03-19 22:36:16.925838", "failed_when_result": false, "rc": 0, "start": "2020-03-19 22:36:16.509638", "stderr": "", "stderr_lines": [], "stdout": "litmusresult.litmus.io/project-account-resources-check configured", "stdout_lines": ["litmusresult.litmus.io/project-account-resources-check configured"]}

TASK [Generate the litmus result CR to reflect EOT (End of Test)] **************
skipping: [127.0.0.1] => {"changed": false, "skip_reason": "Conditional result was False"}

TASK [Analyze the cr yaml] *****************************************************
skipping: [127.0.0.1] => {"changed": false, "skip_reason": "Conditional result was False"}

TASK [Apply the litmus result CR] **********************************************
skipping: [127.0.0.1] => {"changed": false, "skip_reason": "Conditional result was False"}

TASK [set_fact] ****************************************************************
ok: [127.0.0.1] => {"ansible_facts": {"director_url": "http://35.237.220.153:30380"}, "changed": false}

TASK [Get username] ************************************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "cat /etc/secret-volume/username", "delta": "0:00:00.002959", "end": "2020-03-19 22:36:17.335930", "rc": 0, "start": "2020-03-19 22:36:17.332971", "stderr": "", "stderr_lines": [], "stdout": "DCEF255D1CBE7C899FC2", "stdout_lines": ["DCEF255D1CBE7C899FC2"]}

TASK [Get password] ************************************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "cat /etc/secret-volume/password", "delta": "0:00:00.003044", "end": "2020-03-19 22:36:17.538921", "rc": 0, "start": "2020-03-19 22:36:17.535877", "stderr": "", "stderr_lines": [], "stdout": "3y2b3ysFvRqu5z6VXUDXtqxjyQ7yjhMkhLKfTnvS", "stdout_lines": ["3y2b3ysFvRqu5z6VXUDXtqxjyQ7yjhMkhLKfTnvS"]}

TASK [Fetch pool pods from cluster] ********************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "kubectl get pods -n openebs | grep cstor | awk '{print $1}'", "delta": "0:00:00.073955", "end": "2020-03-19 22:36:17.823474", "rc": 0, "start": "2020-03-19 22:36:17.749519", "stderr": "", "stderr_lines": [], "stdout": "cstor-sparse-pool-i2rt-576b79f77-tg4x8\ncstor-sparse-pool-vji4-7cc79f4b9c-85c6z\ncstor-sparse-pool-zua6-6959d84649-fzn8n", "stdout_lines": ["cstor-sparse-pool-i2rt-576b79f77-tg4x8", "cstor-sparse-pool-vji4-7cc79f4b9c-85c6z", "cstor-sparse-pool-zua6-6959d84649-fzn8n"]}

TASK [Get cluster pool resources for ProjectAccount] ***************************
changed: [127.0.0.1] => {"changed": true, "cmd": "python3 /api_testing/group/access.py --username DCEF255D1CBE7C899FC2 --password 3y2b3ysFvRqu5z6VXUDXtqxjyQ7yjhMkhLKfTnvS --account ProjectAccount --url http://35.237.220.153:30380 --resource pool", "delta": "0:00:00.230418", "end": "2020-03-19 22:36:18.266069", "rc": 0, "start": "2020-03-19 22:36:18.035651", "stderr": "", "stderr_lines": [], "stdout": "cstor-sparse-pool-i2rt-576b79f77-tg4x8\ncstor-sparse-pool-vji4-7cc79f4b9c-85c6z\ncstor-sparse-pool-zua6-6959d84649-fzn8n", "stdout_lines": ["cstor-sparse-pool-i2rt-576b79f77-tg4x8", "cstor-sparse-pool-vji4-7cc79f4b9c-85c6z", "cstor-sparse-pool-zua6-6959d84649-fzn8n"]}

TASK [Get cluster application resources for ProjectAccount] ********************
changed: [127.0.0.1] => {"changed": true, "cmd": "python3 /api_testing/group/access.py --username DCEF255D1CBE7C899FC2 --password 3y2b3ysFvRqu5z6VXUDXtqxjyQ7yjhMkhLKfTnvS --account ProjectAccount --url http://35.237.220.153:30380 --resource maya-app", "delta": "0:00:00.167352", "end": "2020-03-19 22:36:18.646222", "rc": 0, "start": "2020-03-19 22:36:18.478870", "stderr": "", "stderr_lines": [], "stdout": "mongo", "stdout_lines": ["mongo"]}

TASK [Check if cluster pool pods is same as Project Account pool pod resources] ***
changed: [127.0.0.1] => {"changed": true, "cmd": "echo \"pool pods list found on the cluster is same as director project account pool pods resources\"", "delta": "0:00:00.002754", "end": "2020-03-19 22:36:18.848963", "failed_when_result": false, "rc": 0, "start": "2020-03-19 22:36:18.846209", "stderr": "", "stderr_lines": [], "stdout": "pool pods list found on the cluster is same as director project account pool pods resources", "stdout_lines": ["pool pods list found on the cluster is same as director project account pool pods resources"]}

TASK [Fetch statefulset applications from cluster] *****************************
changed: [127.0.0.1] => (item=app-mongo-ns) => {"ansible_loop_var": "item", "attempts": 1, "changed": true, "cmd": "kubectl get sts -n app-mongo-ns --no-headers | awk '{print $1}'", "delta": "0:00:00.099717", "end": "2020-03-19 22:36:19.202387", "item": "app-mongo-ns", "rc": 0, "start": "2020-03-19 22:36:19.102670", "stderr": "", "stderr_lines": [], "stdout": "mongo", "stdout_lines": ["mongo"]}

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
changed: [127.0.0.1] => {"changed": true, "checksum": "b332b11a40bc15e85b3593c4f26481a84f0c3ac0", "dest": "./litmus-result.yaml", "gid": 0, "group": "root", "md5sum": "80369ad7dcad5304e04153805f731541", "mode": "0644", "owner": "root", "size": 428, "src": "/root/.ansible/tmp/ansible-tmp-1584657379.5231578-281039215641021/source", "state": "file", "uid": 0}

TASK [Analyze the cr yaml] *****************************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "cat litmus-result.yaml", "delta": "0:00:00.003450", "end": "2020-03-19 22:36:20.055407", "rc": 0, "start": "2020-03-19 22:36:20.051957", "stderr": "", "stderr_lines": [], "stdout": "---\napiVersion: litmus.io/v1alpha1\nkind: LitmusResult\nmetadata:\n\n  # name of the litmus testcase\n  name: project-account-resources-check \nspec:\n\n  # holds information on the testcase\n  testMetadata:\n    app:  \n    chaostype:  \n\n  # holds the state of testcase,  manually updated by json merge patch\n  # result is the useful value today, but anticipate phase use in future \n  testStatus: \n    phase: completed  \n    result: Pass ", "stdout_lines": ["---", "apiVersion: litmus.io/v1alpha1", "kind: LitmusResult", "metadata:", "", "  # name of the litmus testcase", "  name: project-account-resources-check ", "spec:", "", "  # holds information on the testcase", "  testMetadata:", "    app:  ", "    chaostype:  ", "", "  # holds the state of testcase,  manually updated by json merge patch", "  # result is the useful value today, but anticipate phase use in future ", "  testStatus: ", "    phase: completed  ", "    result: Pass "]}

TASK [Apply the litmus result CR] **********************************************
changed: [127.0.0.1] => {"changed": true, "cmd": "kubectl apply -f litmus-result.yaml", "delta": "0:00:00.149529", "end": "2020-03-19 22:36:20.464894", "failed_when_result": false, "rc": 0, "start": "2020-03-19 22:36:20.315365", "stderr": "", "stderr_lines": [], "stdout": "litmusresult.litmus.io/project-account-resources-check configured", "stdout_lines": ["litmusresult.litmus.io/project-account-resources-check configured"]}

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
