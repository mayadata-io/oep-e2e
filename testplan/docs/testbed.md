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

## Cluster details used in Soak testing



Different clusters are used on different platforms. Hence the clusters are descibed on per platform basis.

### GCP

### OnPrem-Konvoy

### OnPrem-Rancher

### AWS

