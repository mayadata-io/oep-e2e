### File .master-plan.yaml

_.master-plan.yaml_ file will contain all the desired test cases for OEP platform. Detailed testcases are derived from this master plan. Detailed testcases will be placed in the repo with enough hints to trace it back to this testcase id.


Following is a sample master plan yaml:

```yaml
kind: MasterPlan
apiVersion: e2e.mayadata.io/v1alpha1
metadata:
    name: masterTestplan
spec:
    tests:
    - tcid: "TCID-DIR-INSTALL-OPENEBS"
      name: "Install OpenEBS on a Director Onprem Cluster"
      description: "Test the components are installed properly using both backend and Director apis. Check from the status from status agent response for the OpenEBS components."
      labels:
        test/feature: "Install and Upgrade of OpenEBS"
        test/subFeature: "Install OpenEBS ControlPlane"
        test/priority: "P0"
        git/location: Add the actual link to TC readme"
        test/status: "Not Automated"

    - tcid: "TCID-DIR-CONNECT-INSTALL-OPENEBS"
      name: "Install OpenEBS on a K8S Cluster connected to Director Onprem Cluster"
      description: "Optional skipping here"
      labels:
        test/feature: "Install and Upgrade of OpenEBS"
        test/subFeature: "Install OpenEBS ControlPlane"
        test/priority: "P0"
        git/location: "Add the actual link to TC readme"
        test/status: "Not Automated"
```


### TCID format

Each test case would be specified in individual gitlab jobs in gitlab-ci.yaml. Actual test case would be having this unique id prefixed . Each test case would have a separate readme. The tcid will be in capital case.

A _TCID_ can be constructed as TCID-COMPONENT-FEATURE-XXX
e.g. TCID-DIR-TEAMING-GUI-ALL refers to all Director teaming testcases implemented via Selenium

_NOTE: One is free to add sub-features & testname to TCID_


| Item                      | Description                    |
| ------------------------- | ------------------------------ |
| DIR                       | Director                       |
| INSTALL-N-UPGRADE         | Install & Upgrade              |
| TEAMING                   | Teaming                        |
| OPENEBS                   | OpenEBS                        |
| OEE                       | OpenEBS Enterprise Edition     |
| OP                        | OpenEBS Provisioning           |
| OO                        | OpenEBS Operator               |
| DMAAS                     | DMAAS                          |
| CSTOR-POOL                | CStor Pool                     |
| JIVA                      | Jiva Volume                    |
| LOCAL-DEV                 | Local Provisioner by Device    |
| LOCAL-HP                  | Local Provisioner by Host Path |
| GUI                       | GUI Automation                 |
| RECOMMEND                 | Recommendations                |
