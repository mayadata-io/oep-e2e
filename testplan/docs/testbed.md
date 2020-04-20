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

## Cluster details used in Testing



Different clusters are used on different platforms. Hence the clusters are described on per platform basis.

### OnPrem-Konvoy

**TODO**

### OnPrem-Rancher

| K8S Cluster | Master              | Worker Nodes                                  | Notes - Cluster Used           |
| -------- | ------------------- | --------------------------------------------- | ----------------------------- |
| Ran-C1 | 1 Node, 16GB, 2 vCPU | 3 Node - Each node 16GB 4 vCPU                | Director Onprem Install       |
| Ran-C2 | 1 Node, 16GB, 2 vCPU | 5 Nodes - Each node  32GB 8CPU, 6x100GB Disks | OpenEBS Install Director      |
| Ran-C3 | 1 Node, 16GB, 2 vCPU | 3 Nodes - Each node  16GB 8CPU, 3x100GB Disks | OpenEBS Install Helm          |
| Ran-C4 | 1 Node, 16GB, 2 vCPU | 1 Node - Each node 16GB 2 vCPU,               | Director Onprem Upgrade       |
| Ran-C5 | 1 Node, 16GB, 2 vCPU | 3 Nodes - Each node  32GB 2CPU, 3x100GB Disks | OpenEBS Install Upgrade       |
| Ran-C6      | 1 Node, 16GB, 2 vCPU | 3 Nodes - Each node  16GB 2CPU, 3x100GB Disks | OpenEBS Install Upgrade       |
| Ran-C7 | 1 Node, 32GB, 4 vCPU | 10Nodes, Each Node 32GB 6vCPU,  6x100GB SSDs  | **Workload Cluster  OpenEBS** |

**Note** -- {C1,C2,C3 }clusters  or {C4,C5,C6} clusters will be running at a point of time. 

C7 will be running always with certain load and continuously upgraded with each release builds.



### AWS

AWS platform will be deployed on managed K8S, 

| K8S    | Master  | Worker Nodes                                     | Notes - Cluster Used     |
| ------ | ------- | ------------------------------------------------ | ------------------------ |
| AWS-C1 | Managed | 1 Node - Each node 16GB 2 vCPU                   | Director Onprem Install  |
| AWS-C2 | Managed | 3 Nodes - Each node  16GB 2CPU, 3x100GB EBS SSDs | OpenEBS Install Director |
| AWS-C3 | Managed | 1 Node - Each node 16GB 2 vCPU                   | Director Onprem Upgrade  |
| AWS-C4 | Managed | 3 Nodes - Each node  16GB 2CPU, 3x100GB EBS SSDs | OpenEBS Install Upgrade  |

**Note --** {C1,C2 }clusters  or {C4,C5,}clusters will be at a point of time. 

## Implementation Phase

As mentioned in [Pipeline](/docs/gitlabstages#implementation-phase)

