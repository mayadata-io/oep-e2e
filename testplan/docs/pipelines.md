---
id: pipelines
title: E2E Pipelines
sidebar_label: Pipelines
---
## OEP E2E Pipeline

OEP E2E pipeline is a GitLab based pipeline. This pipeline is triggered for each OEP release. The images are taken from [director-charts-internal](https://github.com/mayadata-io/director-charts-internal) repo. OEP pipeline is divided into following groups:

- Group 1
- Group 2
- Group 3

### Group 1 (C1, C2, C3)

This group consists of clusters _(C1, C2 & C3)_. These clusters are created followed by installation of latest release of OEP & testing this release. As part of teardown all these clusters are destroyed. [Link to Actual Image](https://docs.google.com/drawings/d/16e98Ty_LV0UwGJLIyiMung6DLoIbaQimfOUwvQtnAko/edit)

![Step 1](https://docs.google.com/drawings/d/e/2PACX-1vS-SVez5ufcMTQTuvZAYrL4cFYaw7E0t57QB4Ega-OZjY1UTs0v2QPRaJZB4sdbHauBTEvvgWlviGzP/pub?w=788&h=245)

Group 1 consists of following _GitLab stages_:

- **Cluster Create**
    - Three kubernetes clusters are created namely **C1**, **C2**, & **C3**.
    - Details of these clusters are found in [Testbed](testbed.md)
- **Install**
    - In this stage OEP components are installed
    - C1 would be installed with latest version of DOP
    - C2 and C3 are connected to C1 using DOP APIs
    - OpenEBS Enterprise is installed on C2 using DOP
    - OpenEBS Enterprise is installed on C3 using Helm
- **Test**
    - Functional Tests
    - Chaos Tests
    - Scalability Tests
- **Cluster Cleanup**
    - All clusters i.e. C1, C2, C3 are destroyed

### Group 2 (C4, C5, C6)

_NOTE: Group 2 is run only if **group 1** completes successfully_

Group 2 consists of clusters 4, 5 & 6. Group 2 involves creation of clusters & installation of **previous** stable version of OEP. Actual testing involves upgrade of OEP to its latest release. This stage is marked as complete upon successful teardown of the clusters. [Link to Actual Image](https://docs.google.com/drawings/d/1oaYLnNQXHIfBn7Jwr5K1N5PDdEhi2yE2jd4gFjbrC8o/edit)

![Upgrade Pipeline](https://docs.google.com/drawings/d/e/2PACX-1vSVDOO2JapUeVuoiSufGaISwuZufvB-F6X8x1Xsns3EUN0piW_b14cKHlYNZzJn3YvI7zc1jvR302Dv/pub?w=955&h=283)

Group 2 consists of followin _Gitlab Stages_:

- **Cluster Create**
    - Three kubernetes clusters are created namely **C4**, **C5**, **C6**
    - Details of these clusters are found in [Testbed](testbed.md)
- **Install Previous**
    - C4 is installed with **previous** stable version of DOP using DOP's helm chart
    - C5 and C6 is connected to C1 using DOP APIs
    - Last stable version of OpenEBS Enterprise is installed on C5 using DOP
    - Last stable version of OpenEBS Enterprise is installed on C6 using Helm
- **Upgrade To Latest**
    - DOP in C4 is upgraded using DOP's helm chart
    - OpenEBS Enterprise in C5 is upgraded using DOP APIs
    - OpenEBS Enterprise in C6 is upgraded using OpenEBS Enterprise helm chart
- **Test** 
    - Functional Tests
    - Chaos Tests
    - Scalability Tests
- **Cluster Cleanup**
    - All clusters i.e. C4, C5, C6 are destroyed

### Group 3 (C7)

_NOTE: Group 3 is run only if **group 2** completes successfully._

Group 3 runs SOAK tests. It consists of long running cluster(s) with some applications & loads running against these applications. These clusters try to be as close as possible to any customer's environment. [Link to Actual Image](https://docs.google.com/drawings/d/1oqMYd80X4Vf2hIpkXhNNPGTBBsr8JYQGGi06UHbr0pY/edit)

![Soak Test Pipeline](https://docs.google.com/drawings/d/e/2PACX-1vS56imUpkbH74X0f3Ty46dyAMQw_2EEm0eLjq1wp5K38GuR4db-QL7zdlSLsp5xqaeX4Po2Ig2n6w1Z/pub?w=741&h=232)

Group 3 consists of following _Gitlab stages_:

- **Import Stage**
    - Cluster C7 is connected to DOP running in **C4**
    - _NOTE: C7 cluster is never brought down_
    - _NOTE: C7 cluster is always upgraded to latest release_
- **Upgrade To Latest**
    - OpenEBS Enterprise is upgraded to latest version using DOP APIs
- **Test**
    - Functional Tests
    - Chaos Tests
    - Scalability Tests

_NOTE: SOAK clusters are also known as **workload** clusters_


### Pipeline Clusters

#### Group 1

- Clusters 1, 2 & 3 belong to this group
- AWS, Rancher & Konvoy are the supported platforms in group 1
- All the clusters are destroyed at the end of this group run
- Cluster **1** is installed with DOP
- Cluster **2** and cluster **3** are connected to cluster **1** via DOP


| Platform | Cluster | Installation    | Remarks                                        |
| -------- | ------- | --------------  | ---------------------------------------------- |
| AWS      | AWS-C1  | DOP             |                                                |
| AWS      | AWS-C2  | OpenEBS via DOP | AWS-C2 connected to AWS-C1. Run Director tests |
| AWS      | AWS-C3  | OpenEBS via Helm| AWS-C3 connected to AWS-C1. Run OpenEBS tests  |
| Rancher  | Ran-C1  | DOP             |                                                |
| Rancher  | Ran-C2  | OpenEBS via DOP | Ran-C2 connected to Ran-C1. Run Director tests |
| Rancher  | Ran-C3  | OpenEBS via Helm| Ran-C3 connected to Ran-C1. Run OpenEBS tests  |
| Konvoy   | Kon-C1  | DOP             |                                                |
| Konvoy   | Kon-C2  | OpenEBS via DOP | Kon-C2 connected to Kon-C1. Run Director tests |
| Konvoy   | Kon-C3  | OpenEBS via Helm| Kon-C3 connected to Kon-C1. Run OpenEBS tests  |


#### Group 2

Group 2 clusters are created with **previous** version of OEP and are destroyed at the end of the stage. Cluster **5** and Cluster **6** is connected to Cluster **4** via DirectorOnPrem _(DOP)_.

_**Note** - Cluster 4, 5, & 6 is brought up from the last snapshots of Cluster 1, 2 & 3._
_**Note** - Last snapshot implies the state of cluster that was used to run previous version of OEP_
_**Note** - New snapshots are taken after running group 1 successfully_

Upgrades will be tested for **previous two releases**. In other words, while testing OEP of version **V**, group 2 will execute following strategies:
- Rancher would be brought up with OEP version V-1 _(i.e. latest but one)_ & upgraded to latest
- Konvoy would be brought up with OEP version V-2 _(i.e. latest but two)_ & upgraded to latest

| Platform| Cluster| Installation    | Ver | Remarks                                        |
| --------| ------ | --------------- | --- | ---------------------------------------------  |
| Rancher | Ran-C4 | DOP             | V-1 |                                                |
| Rancher | Ran-C5 | OpenEBS via DOP | V-1 | Ran-C2 connected to Ran-C4. Run Director tests |
| Rancher | Ran-C6 | OpenEBS via Helm| V-1 | Ran-C3 connected to Ran-C4. Run OpenEBS tests  |
| Konvoy  | Kon-C4 | DOP             | V-2 |                                                |
| Konvoy  | Kon-C5 | OpenEBS via DOP | V-2 | Kon-C5 connected to Kon-C4. Run Director tests |
| Konvoy  | Kon-C6 | OpenEBS via Helm| V-2 | Kon-C6 connected to Kon-C4. Run OpenEBS tests  |


#### Group 3
Group 3 cluster i.e cluster 7 is dedicated for soak testing. These clusters are known as workload clusters. A workload cluster is never shutdown. This cluster is only upgraded to new OEP releases.

| Platform  | Cluster | Installation     | Remarks                    |
| --------- | ------- | -----------      | -------------------------- |
| Rancher   | Ran-C1  | DOP              |                            |
| Rancher   | Ran-C7  | OpenEBS via HELM | Ran-C7 connected to Ran-C1 |

## GitLab Stages

Following GitLab stages take part in one or more groups mentioned above:

**Cluster Setup**

Setup the cluster, underlying disks, networks or any pre-requisites that need to be done. This is not counted as a test case and hence is not calculated for coverage.

**Install or Upgrade Tesing**

Director installation test cases, upgrade cases, day 2 operations of director, chaos tests around director are done in this stage.

**Functional Tests**

There are a set of tests that are written against REST api. All functional, scalable and chaos testing written using these APIs will be under this stage. A separate user cluster or many user clusters are connected to Director for the tests under this stage.

**Functional Testing via Selenium**

All the tests written using GUI automation or Selenium will be under this stage. A separate user cluster or many user clusters are connected to Director for the tests under this stage.

**Functional tests  for Storage components **

There are a set of tests that are written against storage components.  A separate user cluster or many user clusters are connected to Director for the tests under this stage.

**Cluster tear down**

E2E metrics, finalizing the tests, disconnect the user clusters,clean up resources, delete Director OnPrem and scaledown/destroy cluster where DOP is installed.


#### Kubera PR workflow as one of the use case:

- Staging Branch (Staging Kubera Director) release--1.11 . PR are merged on daily basis.
- E2E team tests the Staging branch in a release cycle  
- PR are cherry picked into preprod (Prepod Kubera Director), release--1.11 (June10) (Not tested by E2E).
- PR are cherry picked into master (Kubera Director) release--1.11 (June15) (Tested by E2E).
- PR are cherry picked into enterprise-master (KDOP) release--1.11 (June16 RC1, July15) -- OEP release branch get tested by E2E. [OEP-Release](https://oep-pipelines.mayadata.io/) .

- Director ci image testing on daily basis can be seen on [ci.mayadata.io](https://ci.mayadata.io/) .

