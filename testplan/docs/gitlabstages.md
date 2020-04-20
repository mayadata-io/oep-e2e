---
id: gitlabstages
title: E2E Pipelines
sidebar_label: Pipelines
---
------

## Gitlab

OEP E2E is done using GitLab. Each release build of OEP will trigger the following stages. It is also possible to trigger the pipelines manually.  Different pipelines run in OEP are as listed below.

- Install Pipeline
- Upgrade Pipeline
- Soak Test Bed pipeline

## GitLab Stages

Following are the suggested stages for each pipeline.

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



## OEP E2E Pipelines
OEP pipeline can be divided into following stages, each stage can have multiple stages as mentioned above
- Install
- Upgrade
- Soak Test

### Install Stage

Setups are created and the current version of OEP components are installed and tested and post this clusters are deleted as part of the stage [Link to Actual Image](https://docs.google.com/drawings/d/16e98Ty_LV0UwGJLIyiMung6DLoIbaQimfOUwvQtnAko/edit)

![Install Pipeline Image](https://docs.google.com/drawings/d/e/2PACX-1vS-SVez5ufcMTQTuvZAYrL4cFYaw7E0t57QB4Ega-OZjY1UTs0v2QPRaJZB4sdbHauBTEvvgWlviGzP/pub?w=788&h=245)


### Upgrade Stage
This stage would be run only if the Install Pipeline is successful. Setups are created, the prior version of OEP components are installed and then upgraded and deleted as part of the stage. [Link to Actual Image](https://docs.google.com/drawings/d/1oaYLnNQXHIfBn7Jwr5K1N5PDdEhi2yE2jd4gFjbrC8o/edit)

![Upgrade Pipeline](https://docs.google.com/drawings/d/e/2PACX-1vSVDOO2JapUeVuoiSufGaISwuZufvB-F6X8x1Xsns3EUN0piW_b14cKHlYNZzJn3YvI7zc1jvR302Dv/pub?w=955&h=283)

### Soak Test Stage

This stagee would be run only if the upgrade pipeline is successful. Setups are already present with some load running. This is to create a customer environment. [Link to Actual Image](https://docs.google.com/drawings/d/1oqMYd80X4Vf2hIpkXhNNPGTBBsr8JYQGGi06UHbr0pY/edit)

![Soak Test Pipeline](https://docs.google.com/drawings/d/e/2PACX-1vS56imUpkbH74X0f3Ty46dyAMQw_2EEm0eLjq1wp5K38GuR4db-QL7zdlSLsp5xqaeX4Po2Ig2n6w1Z/pub?w=741&h=232)



### Test Setups

#### Install Pipeline

The following test setups are created on each platform and cleaned-up at the end of the pipeline. Cluster2 and Cluster3 would be connected to Cluster1 DOP for provisioning and monitoring.



| Platform    | Cluster  | K8S Version | Installation         | Remarks                                                      |
| ----------- | -------- | ----------- | -------------------- | ------------------------------------------------------------ |
| AWS         | Cluster1 | V 1.14      | Onprem Director      |                                                              |
|             | Cluster2 | V 1.14      | OpenEBS via Director | Cluster 2 will be connected to Cluster1.  Director Specific Tests |
|             | Cluster3 | V 1.16      | OpenEBS via Helm     | Cluster 3 will be connected to Cluster2.  OpenEBS specific Tests including OpenEBS CE pipeline |
| Rancher LAB | Cluster1 | V 1.14      | Onprem Director      |                                                              |
|             | Cluster2 | V 1.14      | OpenEBS via Director | Cluster 2 will be connected to Cluster1. Director Specific Tests |
|             | Cluster3 | V 1.16      | OpenEBS via Helm     | Cluster 3 will be connected to Cluster2. OpenEBS specific Tests including OpenEBS CE pipeline |
| Konvoy Lab  | Cluster1 | V 1.14      | Onprem Director      |                                                              |
|             | Cluster2 | V 1.14      | OpenEBS via Director | Cluster 2 will be connected to Cluster1. Director Specific Tests |
|             | Cluster3 | V 1.16      | OpenEBS via Helm     | Cluster 3 will be connected to Cluster2. OpenEBS specific Tests including OpenEBS CE pipeline |



#### Upgrade Pipeline

The following test setups are created with prior versions on each platform and cleaned-up at the end of the pipeline. Cluster2 and Cluster3 would be connected to Cluster1 DOP for provisioning and monitoring. 

For Example, say **The current version is 1.11**

| Platform    | Cluster  | K8S Version | Installation                   | Installed version | Remarks                                                      |
| ----------- | -------- | ----------- | ------------------------------ | ----------------- | ------------------------------------------------------------ |
| Rancher LAB | Cluster4 | V 1.14      | Onprem Director	Version 1.9 |                   |                                                              |
|             | Cluster5 | V 1.14      | OpenEBS via Director           | Version 1.9       | Cluster 2 will be connected to Cluster1. Director Specific Tests |
|             | Cluster6 | V 1.16      | OpenEBS via Helm               | Version 1.9       | Cluster 3 will be connected to Cluster2. OpenEBS specific Tests including OpenEBS CE pipeline |
| Konvoy Lab  | Cluster4 | V 1.14      | Onprem Director                | Version 1.10      |                                                              |
|             | Cluster5 | V 1.14      | OpenEBS via Director           | Version 1.10      | Cluster 2 will be connected to Cluster1. Director Specific Tests |
|             | Cluster6 | V 1.16      | OpenEBS via Helm               | Version 1.10      | Cluster 3 will be connected to Cluster2. OpenEBS specific Tests including OpenEBS CE pipeline |



#### Soak Testing Pipeline
The workload cluster will be used for Soak Testing. This would be always running. Any new builds will be upgraded to this and continue testing on the same.

| Platform                     | K8S                  | Installation     | Remarks                                                      |
| ---------------------------- | -------------------- | ---------------- | ------------------------------------------------------------ |
| Rancher                      | Rancher              | Onprem Director  |                                                              |
| Ubuntu-16.4 K8s-Version 1.16 | Generic version 1.16 | OpenEBS Via Helm | Workload Clusters. This Cluster will be connected to above Onprem Cluster |


## Implementation Phase

Pipelines would be implemented in the following way
#### Phase 1 (AWS, Rancher) (OEP 1.9)
- Install Stage : Cluster1 would be installed with DOP, Cluster2 would be connected to Director and OpeneEBS would be installed using Director and Functional Tests of Both Director and OpenEBS would be run in seperate Gitlab stage.
#### Phase 2 (AWS, Rancher) (OEP 1.10)
- Install Stage: Cluster 3 OpenEBS installed with Helm. 
- Upgrade stage would be incorporated.
#### Phase 3 (AWS, Rancher) (OEP 1.10)
- Workload Stage : This would be added into pipeline.
