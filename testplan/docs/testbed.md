---
id: testbed
title: OEP E2E TestBed
sidebar_label: Testbed
---
------


Pipelines are run sequentially on different platforms. The results are aggregated at <a href="https://oep-pipelines.mayadata.io/" target="_blank">oep-pipelines.mayadata.io</a>


## Testbed diagram ([Original file for editing](https://docs.google.com/drawings/d/1zVjph5xAyXNuQm81wv43NaH-WSaH1hIiqyNYot2oTOQ/edit?usp=sharing))

![OEP E2E Testbed](https://docs.google.com/drawings/d/e/2PACX-1vSNvpvyPnyvHFTwJXT1E_M-KMydF3z5t3um_lCDSAEfbavDBFVkYFZVvu5G90yq7oZCZI0Jv_8kEMj_/pub?w=960&h=720)

## Cluster details used in Testing

There are dedicated clusters for various kubernetes platforms. 

### OnPrem-Konvoy

**TODO**

### OnPrem-Rancher

| Cluster| Master               | Worker Nodes                       | Notes                   |
| -------| -------------------  | -------------------------          | ----------------------  |
| Ran-C1 | 1 Node, 16GB, 2 vCPU | 3 nodes x 16GB 4 vCPU              | DOP                     |
| Ran-C2 | 1 Node, 16GB, 2 vCPU | 5 nodes x 32GB 8CPU, 6x100GB Disks | OpenEBS via DOP         |
| Ran-C3 | 1 Node, 16GB, 2 vCPU | 3 nodes x 16GB 8CPU, 3x100GB Disks | OpenEBS via Helm        |
| Ran-C4 | 1 Node, 16GB, 2 vCPU | 1 node 16GB 2 vCPU                 | DOP Upgrade             |
| Ran-C5 | 1 Node, 16GB, 2 vCPU | 3 nodes x 32GB 2CPU, 3x100GB Disks | OpenEBS Upgrade via DOP |
| Ran-C6 | 1 Node, 16GB, 2 vCPU | 3 nodes x 16GB 2CPU, 3x100GB Disks | OpenEBS Upgrade via Helm|
| Ran-C7 | 1 Node, 32GB, 4 vCPU | 10 nodes x 32GB 6vCPU, 6x100GB SSDs| SOAK cluster via Helm   |

**NOTE**: Either _C1, C2, & C3_ clusters  or _C4,C5, & C6_ clusters will be running at any point of time. 
**NOTE**: SOAK cluster is also known as WORKLOAD cluster
**NOTE**: C7 is the SOAK cluster which runs continuously & gets upgraded with latest releases

### AWS

AWS platform will be deployed on managed kubernetes

| Cluster| Master  | Worker Nodes                                  | Notes                    |
| ------ | ------- | --------------------------------------------- | --------------------     |
| AWS-C1 | Managed | 1 Node 16GB 2 vCPU                            | DOP                      |
| AWS-C2 | Managed | 3 Nodes x 16GB 2CPU, 3x100GB EBS SSDs         | OpenEBS via DOP          |
| AWS-C3 | Managed | 1 Node 16GB 2 vCPU                            | DOP Upgrade              |
| AWS-C4 | Managed | 3 Nodes x 16GB 2CPU, 3x100GB EBS SSDs         | OpenEBS Upgrade via Helm |

**Note** Either _C1 & C2_ clusters  or _C4 & C5_ clusters will be running at any point of time. 

## Implementation Phase

As mentioned in [Pipeline](/docs/gitlabstages#implementation-phase)

