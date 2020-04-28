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

| Cluster | Master               | Worker Nodes                                                 | Notes                    |
| ------- | -------------------- | ------------------------------------------------------------ | ------------------------ |
| Kon-C1  | 1 Node, 16GB, 4vCPU  | 5 nodes, 16GB 4 vCPU, 1x100GB for OS Disks                   | DOP                      |
| Kon-C2  | 1 Node, 32GB, 6vCPU  | 5 nodes x 64GB 12CPU, 1x100GB for OS Disks                         Node1, Node2 and Node3 each of them will have additional disks of total 600GB | OpenEBS via DOP

### OnPrem-Rancher

| Cluster | Master               | Worker Nodes                                                 | Notes                    |
| ------- | -------------------- | ------------------------------------------------------------ | ------------------------ |
| Ran-C1  | 1 Node, 16GB, 4vCPU  | 3 nodes, 16GB 4 vCPU, 1x100GB for OS Disks                   | DOP                      |
| Ran-C2  | 1 Node, 16GB, 4vCPU  | 5 nodes x 32GB 8CPU, 1x100GB for OS Disks.                        Node1, Node2 and Node3 each of them will have additional disks 13*20GB Disks | OpenEBS via DOP          |
| Ran-C3  | 1 Node, 16GB, 4vCPU  | 5 nodes x 32GB 8CPU, 1x100GB Disks for OS.                        Node1, Node2 and Node3 each of them will have additional disks 13*20GB Disks | OpenEBS via Helm         |
| Ran-C4  | 1 Node, 16GB, 4vCPU  | 1 node 16GB 2 vCPU                                           | DOP Upgrade              |
| Ran-C5  | 1 Node, 16GB, 4vCPU  | 5 nodes x 32GB 8CPU, 1x100GB Disks for OS.                        Node1, Node2 and Node3 each of them will have additional disks 13*20GB Disks | OpenEBS Upgrade via DOP  |
| Ran-C6  | 1 Node, 16GB, 4vCPU  | 5 nodes x 32GB 8CPU, 1x100GB Disks for OS.                        Node1, Node2 and Node3 each of them will have additional disks 13*20GB Disks | OpenEBS Upgrade via Helm |
| Ran-C7  | 1 Node, 32GB, 8 vCPU | 10 nodes Node1, Node2, Node3, Node4, Node5, Node6 64GB 12vCPU, 9x100GB SSDs, 1x500GBSSD, 1x300GBSSD, 3x200GBSSDs.                     Node7, Node8, Node9, Node10 has 32GB and 8vCPU | SOAK cluster via Helm    |

**NOTE**: Either _C1, C2, & C3_ clusters  or _C4,C5, & C6_ clusters will be running at any point of time. 
**NOTE**: SOAK cluster is also known as WORKLOAD cluster
**NOTE**: C7 is the SOAK cluster which runs continuously & gets upgraded with latest releases

### AWS

AWS platform will be deployed on managed kubernetes

| Cluster | Nodes                                               | Notes                    |
| ------- | --------------------------------------------------- | ------------------------ |
| AWS-C1  | 4 Nodes, 16GB  4vCPU each node                      | DOP                      |
| AWS-C2  | 4 Nodes,  32GB 4CPU, 9x20GB EBS Disks  in each node | OpenEBS via DOP          |
| AWS-C3  | 4 Nodes,  16GB 4CPU, 9x20GB EBS Disks  in each node | OpenEBS via Helm         |
| AWS-C4  | 4 Node, 16GB  4vCPU each node                       | DOP Upgrade              |
| AWS-C5  | 4 Nodes,  32GB 4CPU, 9x20GB EBS Disks  in each node | OpenEBS Upgrade via DOP  |
| AWS-C6  | 4 Nodes,  16GB 4CPU, 9x20GB EBS Disks  in each node | OpenEBS Upgrade via Helm |

**Note** Either _C1 ,C2,C3_ clusters  or _C4 ,C5,C6_ clusters will be running at any point of time. 

