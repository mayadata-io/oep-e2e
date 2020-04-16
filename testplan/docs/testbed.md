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

### OnPrem-Rancher

| K8S      | Master              | Worker Nodes                                  | Resources                     |
| -------- | ------------------- | --------------------------------------------- | ----------------------------- |
| Cluster1 | 1 Node 16GB 2  vCPU | 3 Node - Each node 16GB 4 vCPU                | Director Onprem Install       |
| Cluster2 | 1 Node 16GB 2  vCPU | 5 Nodes - Each node  32GB 8CPU, 6x100GB Disks | OpenEBS Install Director      |
| Cluster3 | 1 Node 16GB 2  vCPU | 3 Nodes - Each node  16GB 8CPU, 3x100GB Disks | OpenEBS Install Helm          |
| Cluster4 | 1 Node 16GB 2  vCPU | 1 Node - Each node 16GB 2 vCPU,               | Director Onprem Upgrade       |
| Cluster5 | 1 Node 16GB 2  vCPU | 3 Nodes - Each node  32GB 2CPU, 3x100GB Disks | OpenEBS Install Upgrade       |
| Cluster6 | 1 Node 16GB 2  vCPU | 3 Nodes - Each node  16GB 2CPU, 3x100GB Disks | OpenEBS Install Upgrade       |
| Cluster7 | 1 Node 32GB, 42vCPU | 10Nodes, Each Node 32GB 6vCPU,  6x100GB SSDs  | **Workload Cluster  OpenEBS** |

**Note** -- Cluster1,2,3 or Cluster4,5,6 will be at a point of time. It can be same machines with cleanup

Cluster7 will be running always with certain load  and continuously upgraded with each release builds.



### AWS

AWS platform will be deployed on managed K8S, 

| K8S      | Master  | Worker Nodes                                     | Resources                |
| -------- | ------- | ------------------------------------------------ | ------------------------ |
| Cluster1 | Managed | 1 Node - Each node 16GB 2 vCPU                   | Director Onprem Install  |
| Cluster2 | Managed | 3 Nodes - Each node  16GB 2CPU, 3x100GB EBS SSDs | OpenEBS Install Director |
| Cluster3 | Managed | 1 Node - Each node 16GB 2 vCPU                   | Director Onprem Upgrade  |
| Cluster4 | Managed | 3 Nodes - Each node  16GB 2CPU, 3x100GB EBS SSDs | OpenEBS Install Upgrade  |

**Note --** Cluster1,2 or Cluster3,4 will be powered on at a point of time.

### GCP (Not planned for now)