---
id: gitlabstages
title: E2E Pipelines
sidebar_label: Pipelines
---
## OEP E2E Pipelines

OEP E2E is done using GitLab. Each release build of OEP will trigger the following test stages. Trigger of the pipelines will be done manually most cases or initiated as part of release builds.  OEP pipeline can be broadly divided into following test stages, each test stage can have multiple gitlab stages as mentioned in [Gitlab Stages](#gitlab-stages) section. 

- Install Test Stage
- Upgrade Test Stage
- Soak Test Test Stage

### Install Test Stage

Setups are created and the current version of OEP components are installed and tested and post this clusters are deleted as part of the stage [Link to Actual Image](https://docs.google.com/drawings/d/16e98Ty_LV0UwGJLIyiMung6DLoIbaQimfOUwvQtnAko/edit)

![Install Pipeline Image](https://docs.google.com/drawings/d/e/2PACX-1vS-SVez5ufcMTQTuvZAYrL4cFYaw7E0t57QB4Ega-OZjY1UTs0v2QPRaJZB4sdbHauBTEvvgWlviGzP/pub?w=788&h=245)

The Install Test Stage will have the following Gitlab Stages

- Cluster Create - 3 K8S clusters would be created namely C1, C2, C3 as configuration mentioned in [Testbed](testbed.md)
- Install Stage -- 
  - In this setup of OEP components would be installed and setup. 
  - C1 would be installed with DOP. 
  - C2 and C3 would be connected to C1 using DOP APIs.
  - OpenEBS Enterprise would be installed on C2 using DOP
  - OpenEBS Enterprise would be installed on C3 using Helm
- Functional Test -Actual Functionality tests, would be created as per the Test Straegy in the [e2e paln](https://e2e.mayadata.io)
  - Functional Tests
  - Chaos Tests
  - Scalability Tests
- Cluster Cleanup  - Cluster created would be destroyed in this stage.

### Upgrade Test Stage

This stage would be run only if the Install stage is successful. Setups are created, the prior version of OEP components are installed and then upgraded and deleted as part of the stage. [Link to Actual Image](https://docs.google.com/drawings/d/1oaYLnNQXHIfBn7Jwr5K1N5PDdEhi2yE2jd4gFjbrC8o/edit)

![Upgrade Pipeline](https://docs.google.com/drawings/d/e/2PACX-1vSVDOO2JapUeVuoiSufGaISwuZufvB-F6X8x1Xsns3EUN0piW_b14cKHlYNZzJn3YvI7zc1jvR302Dv/pub?w=955&h=283)

The Upgrade Test Stage will have the following Gitlab Stages

- Cluster Create - 3 K8S clusters would be created namely C4, C5, C6 as configuration mentioned in [Testbed](testbed.md)
- Install Stage - In this setup of OEP components would be installed and setup. 
  - C4 would be installed with DOP version mentioned in . 
  - C5 and C6 would be connected to C1 using DOP APIs.
  - OpenEBS Enterprise would be installed on C5 using DOP
  - OpenEBS Enterprise would be installed on C6 using Helm
- Upgrade Stage
  - C4 would be upgrade with DOP helm chart
  - C5 would be upgrade using DOP APIs
  - C6 would be upgrade using helm chart.
- Functional Tests -Actual Functionality tests, would be created as per the Test Straegy in the [e2e paln](https://e2e.mayadata.io)
  - Functional Test cases
  - Chaos Testss

### Soak Test Stage

This stage would be run only if the upgrade pipeline is successful. Setups are already present with some load running. This is to create a customer environment. [Link to Actual Image](https://docs.google.com/drawings/d/1oqMYd80X4Vf2hIpkXhNNPGTBBsr8JYQGGi06UHbr0pY/edit)

![Soak Test Pipeline](https://docs.google.com/drawings/d/e/2PACX-1vS56imUpkbH74X0f3Ty46dyAMQw_2EEm0eLjq1wp5K38GuR4db-QL7zdlSLsp5xqaeX4Po2Ig2n6w1Z/pub?w=741&h=232)

The Soak Test Stage will have the following Gitlab Stages

- C7 working health work load cluster would be imported to DOP. This setup would be continuously running with pre-defined load.  The load/workload will be running on this setup pre, during and post of this stage. This cluster would not be brought down and would be continuously upgraded with each release builds to mimic production work load scenarios. 
- Upgraded to latest version using DOP APIs
- Following tests would be performed
  - Functional Tests like provision
  - Chaos Tests
  - Day2 Operation.



### Test Setups

#### Install Stage Test Setup

The following test setups are created on each platform and cleaned-up at the end of the stage. Cluster2 and Cluster3 would be connected to Cluster1 DOP for provisioning and monitoring. 



| Platform    | Cluster | Installation         | Remarks                                                      |
| ----------- | ------- | -------------------- | ------------------------------------------------------------ |
| AWS         | AWS-C1  | Onprem Director      |                                                              |
|             | AWS-C2  | OpenEBS via Director | Cluster 2 will be connected to Cluster1.  Director Specific Tests |
|             | AWS-C3  | OpenEBS via Helm     | Cluster 3 will be connected to Cluster2.  OpenEBS specific Tests including OpenEBS CE pipeline |
| Rancher LAB | Ran-C1  | Onprem Director      |                                                              |
|             | Ran-C2  | OpenEBS via Director | Cluster 2 will be connected to Cluster1. Director Specific Tests |
|             | Ran-C3  | OpenEBS via Helm     | Cluster 3 will be connected to Cluster2. OpenEBS specific Tests including OpenEBS CE pipeline |
| Konvoy Lab  | Kon-C1  | Onprem Director      |                                                              |
|             | Kon-C2  | OpenEBS via Director | Cluster 2 will be connected to Cluster1. Director Specific Tests |
|             | Kon-C3  | OpenEBS via Helm     | Cluster 3 will be connected to Cluster2. OpenEBS specific Tests including OpenEBS CE pipeline |



#### Upgrade Stage Test Setup

The following test setups are created with prior versions on each platform and cleaned-up at the end of the stage. Cluster2 and Cluster3 would be connected to Cluster1 DOP for provisioning and monitoring. 

For Example, say the current version of OEP is  version **V**

- Rancher would be running with v-1 version of product and upgraded to latest
- Konvoy would be running with v-2 version of prouduct and upgraded to latest.

| Platform    | Cluster | Installation               | Installed version | Remarks                                                      |
| ----------- | ------- | -------------------------- | ----------------- | ------------------------------------------------------------ |
| Rancher LAB | Ran-C4  | Onprem Director	Version | v-1               |                                                              |
|             | Ran-C5  | OpenEBS via Director       | v-1               | Cluster 2 will be connected to Cluster1. Director Specific Tests |
|             | Ran-C6  | OpenEBS via Helm           | v-1               | Cluster 3 will be connected to Cluster2. OpenEBS specific Tests including OpenEBS CE pipeline |
| Konvoy Lab  | Kon-C4  | Onprem Director            | v-2               |                                                              |
|             | Kon-C5  | OpenEBS via Director       | v-2               | Cluster 2 will be connected to Cluster1. Director Specific Tests |
|             | Kon-C6  | OpenEBS via Helm           | v-2               | Cluster 3 will be connected to Cluster2. OpenEBS specific Tests including OpenEBS CE pipeline |



#### Soak Testing Stage Test Setup
The workload cluster will be used for Soak Testing. This would be always running. Any new builds will be upgraded to this and continue testing on the same.

| Platform                     | K8S                  | Installation     | Remarks                                                      |
| ---------------------------- | -------------------- | ---------------- | ------------------------------------------------------------ |
| Rancher                      | Rancher              | Onprem Director  |                                                              |
| Ubuntu-16.4 K8s-Version 1.16 | Generic version 1.16 | OpenEBS Via Helm | Workload Clusters. This Cluster will be connected to above Onprem Cluster |

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
- Install Stage : Cluster1 would be installed with DOP, Cluster2 would be connected to Director and OpeneEBS would be installed using Director and Functional Tests of Both Director and OpenEBS would be run in separate Gitlab stage. 
- Workload cluster would be upgraded manually and connected to Cluster1
#### Phase 2 (AWS, Rancher) (OEP 1.10)
- Install Stage: Cluster 3 OpenEBS installed with Helm. 
- Upgrade stage would be incorporated.
#### Phase 3 (AWS, Rancher) (OEP 1.10)
- Workload Stage : This would be upgraded and added into cluster C1.
