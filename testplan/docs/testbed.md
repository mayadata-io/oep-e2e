---
id: testbed
title: OEP E2E TestBed
sidebar_label: Testbed
---
------



Pipelines are run sequentially on different platforms. The results are aggregated at  <a href="https://ci.mayadata.io/" target="_blank">ci.mayadata.io</a> .



## Testbed diagram ([Original file for editing](https://docs.google.com/drawings/d/1zVjph5xAyXNuQm81wv43NaH-WSaH1hIiqyNYot2oTOQ/edit?usp=sharing))

![OEP E2E Testbed](https://docs.google.com/drawings/d/e/2PACX-1vSNvpvyPnyvHFTwJXT1E_M-KMydF3z5t3um_lCDSAEfbavDBFVkYFZVvu5G90yq7oZCZI0Jv_8kEMj_/pub?w=960&h=720)

[Soak testing](https://en.wikipedia.org/wiki/Soak_testing) is an important part of OEP test plan. There are multiple components to be considered for soak testing. 

- OpenEBS installations on clusters that are connected to Director
- Director On-Prem or DOP itself

Currently, soak testing is being performed only for OpenEBS installations. Applications are deployment closer to the production style on a cluster where OpenEBS is used as storage. As part of the E2E pipeline, this cluster is connected to the Director OnPrem which is installed on the fly. Soak testing for OpenEBS includes mostly day2 operations such as scaling up the capacity, disk fill tests, resizing of the volumes etc.



## Suggested `stages` 

**Cluster setup**

Setup the cluster, underlying disks, networks or any pre-requisites that need to be done. This is not counted as a test case and hence is not calculated for coverage.

**Director Install and upgrade**

Director installation test cases, upgrade cases, day 2 operations of director, chaos tests around director are done in this stage.

**Functional testing with Rest**

There are a set of tests that are written against REST api. All functional, scalable and chaos testing written using these APIs wil be under this stage. A separate user cluster or many user clusters are connected to Director for the tests under this stage.

**Functional testing with Selenium**

All the tests written using GUI automation or Selenium will be under this stage. A separate user cluster or many user clusters are connected to Director for the tests under this stage.

**Cluster tier down**

E2E metrics, finalizing the tests, disconnect the user clusters,clean up resources, delete Director OnPrem and scaledown/destroy cluster where DOP is installed.

