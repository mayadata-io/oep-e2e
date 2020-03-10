# File .master-plan.yaml

The `.master-plan.yaml` file would contain all the desired/known test cases for OEP platform.  From this file detailed testcases would be derived. Testcases will be kept in the repo and would have a unique id `tcid` prefixed.  The excerpt of the file shown below, format has been kept similar to K8S CR.


```kind: MasterPlan
apiVersion: e2e.mayadata.io/v1alpha1
metadata:
  name: masterTestplan
spec:
  tests:
  ### Installation of OpenEBS
  - tcid: "IUOI01"
    name: "Install OpenEBS on a Director Onprem Cluster"
    description: "Test the components are installed properly using both backend and Director apis. Check from the status from status agent response for the OpenEBS components."
    labels:
      test/feature: "Install and Upgrade of OpenEBS"
      test/subFeature: "Install OpenEBS ControlPlane"
      test/priority: "P0"
      git/location: Add the actual link to TC readme"
      test/status: "Not Automated"


  - tcid: "IUOI02"
    name: "Install OpenEBS on a K8S Cluster connected to Director Onprem Cluster"
    description: "Optional skipping here"
    labels:
      test/feature: "Install and Upgrade of OpenEBS"
      test/subFeature: "Install OpenEBS ControlPlane"
      test/priority: "P0"
      git/location: "Add the actual link to TC readme"
      test/status: "Not Automated"

```


## Schema format

##### `tcid` -- referers to a unique id for the testcase. 

Each test case would be called as job in gitlab pipeline using  gitlab-ci.yaml. Actual test case would be having this unique id prefixed . Each test case would have a seperate readme. The tcid will be in lower case.

`tcid` is constructed following, each tcid would be unique and will have 6-7 chars

first two letter indicates the feature.

third and fourth letter indicates the sub feature.

last two chars would be digits in incrementatal way.

Example 

| Feature                   | SubFeature                  |
| ------------------------- | --------------------------- |
| iu -- Install and Upgrade | oi -- OpenEBS Install       |
|                           | oc -- OpenEBS ControlPlane  |
|                           | od -- OpenEBS DataPlane     |
| tr -- Teaming and RBAC    | po -- Project Owner         |
|                           | pa -- Project Admin         |
|                           | pm -- Project Member        |
|                           | pr -- Project ReadOnly User |
|                           | rc -- Role Change |
|                           | iv -- Invite |
| pp -- Pool Provisioning   | cp -- cstor Pool            |

##### `name` --  test case name
##### `description` -- Testcase description
##### `test/subFeature` -- Testcase belong which sub component/feature
##### `test/priority` -- Testcase priority to decide how early it has to be automated. It can have values 0 to 3 where 0 is highest and 3 being lowest.
##### `git/location` -- Location where testcase has been place (link with readme)
##### `test/status` -- Status of TC whether automated or not automated

