---
id: gitlabstages
title: E2E Pipelines
sidebar_label: Pipelines
---
## OEP E2E Pipelines

OEP E2E pipelines are GitLab based pipelines. Each OEP release triggers these pipelines. Some pipelines are triggered manually while others get triggered as part of release builds.  OEP pipeline can be broadly divided into following stages, where each stage can have multiple gitlab stages as mentioned in [Gitlab Stages](#gitlab-stages) section. 

- Install Test Stage
- Upgrade Test Stage
- Soak Test Stage

### Install Test Stage

In this stage, setups are created and latest OEP release is installed & tested. As part of teardown all these clusters are destroyed. [Link to Actual Image](https://docs.google.com/drawings/d/16e98Ty_LV0UwGJLIyiMung6DLoIbaQimfOUwvQtnAko/edit)

![Install Pipeline Image](https://docs.google.com/drawings/d/e/2PACX-1vS-SVez5ufcMTQTuvZAYrL4cFYaw7E0t57QB4Ega-OZjY1UTs0v2QPRaJZB4sdbHauBTEvvgWlviGzP/pub?w=788&h=245)

This stage is further divided into following _GitLab stages_:

- **Cluster Create**
    - Three kubernetes clusters are created namely **C1**, **C2**, & **C3**.
    - Details of these clusters are found in [Testbed](testbed.md)
- **Install Stage**
    - In this stage OEP components are installed
    - C1 would be installed with latest version of DOP
    - C2 and C3 are connected to C1 using DOP APIs
    - OpenEBS Enterprise is installed on C2 using DOP
    - OpenEBS Enterprise is installed on C3 using Helm
- **Execute Tests**
    - Functional Tests
    - Chaos Tests
    - Scalability Tests
    - _Above are defined as test strategies in [e2e plan](https://e2e.mayadata.io)_
- **Cluster Cleanup**
    - All clusters i.e. C1, C2, C3 are destroyed

### Upgrade Test Stage

_NOTE: This stage is run only if **install test stage** is completed successfully_

This stage involves creation of clusters & installation of previous stable OEP version. Actual testing involves upgrade of OEP to its latest release. This stage is marked as complete upon successful teardown of the clusters. [Link to Actual Image](https://docs.google.com/drawings/d/1oaYLnNQXHIfBn7Jwr5K1N5PDdEhi2yE2jd4gFjbrC8o/edit)

![Upgrade Pipeline](https://docs.google.com/drawings/d/e/2PACX-1vSVDOO2JapUeVuoiSufGaISwuZufvB-F6X8x1Xsns3EUN0piW_b14cKHlYNZzJn3YvI7zc1jvR302Dv/pub?w=955&h=283)

This stage is further divided into following _Gitlab Stages_:

- **Cluster Create**
    - Three kubernetes clusters are created namely **C4**, **C5**, **C6**
    - Details of these clusters are found in [Testbed](testbed.md)
- **Install Stage**
  - C4 is installed with last stable version of DOP using DOP's helm chart
  - C5 and C6 would be connected to C1 using DOP APIs
  - Last stable version of OpenEBS Enterprise is installed on C5 using DOP
  - Last stable version of OpenEBS Enterprise is installed on C6 using Helm
- **Upgrade Stage**
  - DOP in C4 is upgraded using DOP's helm chart
  - OpenEBS Enterprise in C5 is upgraded using DOP APIs
  - OpenEBS Enterprise in C6 is upgraded using OpenEBS Enterprise helm chart
- **Execute Tests** 
    - Functional Tests
    - Chaos Tests
    - Scalability Tests
    - _Above are defined as test strategies in [e2e plan](https://e2e.mayadata.io)_
- **Cluster Cleanup**
    - All clusters i.e. C4, C5, C6 are destroyed

### Soak Test Stage

This stage is run only if upgrade test stage is completed successfully. It makes use of long running setups with some running applications & loads running against these applications. This setup tries to be as close as possible to any customer's environment. [Link to Actual Image](https://docs.google.com/drawings/d/1oqMYd80X4Vf2hIpkXhNNPGTBBsr8JYQGGi06UHbr0pY/edit)

![Soak Test Pipeline](https://docs.google.com/drawings/d/e/2PACX-1vS56imUpkbH74X0f3Ty46dyAMQw_2EEm0eLjq1wp5K38GuR4db-QL7zdlSLsp5xqaeX4Po2Ig2n6w1Z/pub?w=741&h=232)

The stage is further divided into following _Gitlab stages_:

- **Import Stage**
    - **C7** workload cluster is connected to DOP running in **C4**
    - _NOTE: C7 cluster is never brought down_
    - _NOTE: C7 cluster is upgraded with latest release_
- **Upgrade Stage**
    - OpenEBS Enterprise is upgraded to latest version using DOP APIs
- **Execute Tests**
    - Functional Tests
    - Chaos Tests
    - Scalability Tests
    - _Above are defined as test strategies in [e2e plan](https://e2e.mayadata.io)_


### Test Setups

#### Install Stage Test Setup

- Test setups are created on each platform
- These setups are destroyed at the end of the stage
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


#### Upgrade Stage Test Setup

The following test setups are created with previous versions on each platform and destroyed at the end of the stage. Cluster **5** and Cluster **6** would be connected to Cluster **4** via Director OnPrem _(DOP)_.

_**Note** - Cluster 4, Cluster 5, Cluster 6 will be brought up from the last snapshots of Cluster 1, Cluster 2 & Cluster 3._
_**Note** - Last snapshot implies the state of cluster that was used to run previous version of OEP_
_**Note** - New snapshots are taken after running install test setup successfully_

Upgrades will be tested for previous two releases. In other words, while testing OEP of version **V**, upgrade stage will execute following strategies:
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


#### Soak Stage Test Setup
Kubernetes workload cluster will be used for soak testing. A workload cluster is the one that is never shutdown. Cluster is upgraded to new OEP releases.

| Platform  | Cluster | Installation     | Remarks                    |
| --------- | ------- | -----------      | -------------------------- |
| Rancher   | Ran-C1  | DOP              |                            |
| Rancher   | Ran-C7  | OpenEBS via HELM | Ran-C7 connected to Ran-C1 |

## GitLab Stages

Following are the suggested stages for each of the Test Stages.

**Cluster setup**

Setup the cluster, underlying disks, networks or any pre-requisites that need to be done. This is not counted as a test case and hence is not calculated for coverage.

**Install or upgrade**

Director installation test cases, upgrade cases, day 2 operations of director, chaos tests around director are done in this stage.

**Functional testing  with Rest**

There are a set of tests that are written against REST api. All functional, scalable and chaos testing written using these APIs will be under this stage. A separate user cluster or many user clusters are connected to Director for the tests under this stage.

**Functional testing with Selenium**

All the tests written using GUI automation or Selenium will be under this stage. A separate user cluster or many user clusters are connected to Director for the tests under this stage.

**Functional tests  for Storage components **

There are a set of tests that are written against storage components.  A separate user cluster or many user clusters are connected to Director for the tests under this stage.

**Cluster tear down**

E2E metrics, finalizing the tests, disconnect the user clusters,clean up resources, delete Director OnPrem and scaledown/destroy cluster where DOP is installed.

## Implementation Phase

Pipelines would be implemented in the following way

#### Phase 1 (AWS, Rancher) (OEP 1.9)
- Install Stage : Cluster1 would be installed with DOP,  Cluster2 would be connected to Director and OpeneEBS would be installed using Director and Functional Tests of Both Director and OpenEBS would be run in separate Gitlab stage. 
- Workload cluster would be upgraded manually and connected to Cluster1
#### Phase 2 (AWS, Rancher) (OEP 1.10)
- Install Stage: Cluster 3 OpenEBS installed with Helm. 
- Upgrade stage using Cluster 4, Cluster5, Cluster6 would be incorporated.
#### Phase 3 (AWS, Rancher) (OEP 1.10)
- Workload Stage : This would be upgraded and added into cluster C1.
