---
id: dao 
title: Data Agility Operators
sidebar_label: Test Strategy
---
------

## DAOs

Data Agility Operators consist of one or more Kubernetes operators that automate OpenEBS operations. They are built using Kubernetes custom resources making them gitops friendly. These can be operated from third party tools as well. Following are current set of DAOs:

- [OpenEBS Operator](https://github.com/mayadata-io/openebs-upgrade)
- [CStorPool Auto](https://github.com/mayadata-io/cstorpoolauto)
- [Storage Provisioner](https://github.com/mayadata-io/storage-provisioner)

## OpenEBS Operator

### TC-DAO-OO-K8S-CLUSTER-MAINTAINANCE
As a DevOps admin, I have openebs installed on a kubernetes cluster. This kubernetes cluster undergoes periodic maintainance. As part of maintaince k8s components are upgraded. This also includes draining of existing nodes & adding new nodes to the cluster. This activity should not impact openebs components & volumes. All the openebs components should work as per the desired specifications. All the openebs volumes should be up & running. All the applications consuming openebs volumes should be up & running.

### TC-DAO-OO-MULTI-TENANCY
As a DevOps admin, I want openebs to enable multi-tenancy in my kubernetes cluster. Each team have their applications running in specific kubernetes namespaces. I would like openebs to extend namespace based multi-tenancy to volumes. In other words, these applications should have their volumes provisioned application namespace. Volumes should consume storage disks granted to specific teams.

### TC-DAO-OO-MULTI-VERSION
As a DevOps admin, I want to rollout storage upgrades in a phased manner to my teams. I want to run multiple versions of openebs in my kubernetes cluster. Each team will be managing their own openebs versions in team's dedicated namespace. Team have their rights to upgrade their specific openebs versions without impacting other teams.

_NOTE: This is an extension of TC-DAO-OO-MULTI-TENANCY_
_NOTE: This will work only when TC-DAO-OO-MULTI-TENANCY works_

| TCID                                                               | Konvoy | GKE  |
| ------------------------------------------------------------------ | ------ | ---- |
| [TC-DAO-OO-K8S-CLUSTER-MAINTAIN](TC-DAO-OO-K8S-CLUSTER-MAINTAIN)   |        |      |
| [TC-DAO-OO-MULTI-TENANCY](TC-DAO-OO-MULTI-TENANCY)                 |        |      |
| [TC-DAO-OO-MULTI-VERSION](TC-DAO-OO-MULTI-VERSION)                 |        |      |

## CStorPool Auto

### TC-DAO-CSPA-K8S-NODE-MAINTAINANCE
As a DevOps admin, I have spinned up a kubernetes cluster using my tools. This cluster includes nodes that are configured with storage disks. These nodes have a life of few days after which they are tore down & new nodes take its place. The storage disks are consumed by cstor pool(s). As part of node recycle, my cstor pool(s) should not be impacted. These cstor pools should discover these new nodes & reconstruct the pool if required. The volumes & corresponding applications consuming these pools should never get impacted.

| TCID                                                            | Konvoy | GKE  |
| --------------------------------------------------------------- | ------ | ---- |
| [TC-DAO-CSPA-K8S-NODE-MAINTAIN](TC-DAO-CSPA-K8S-NODE-MAINTAIN)  | N      | N    |

## StorageProvisioner

### TC-DAO-SP-CI-CD 
As a DevOps admin, I want to provision openebs volumes over the cloud disks. My kubernetes cluster is used for CI CD purposes. The cluster nodes are constantly scaled up and down based on the load from CI CD pipelines. These nodes consume cloud disks which are subsequently consumed by provisioned applications. These cloud disks vary in their speed, persistence type, etc. I would like openebs to manage these disks in my auto scaler setup. My applications should be able to consume disks either as new disks on new nodes or old disks attached to the new nodes post autoscale operation.

| TCID                                                            | Konvoy | GKE  |
| --------------------------------------------------------------- | ------ | ---- |
| [TC-DAO-SP-CI-CD](TC-DAO-SP-CI-CD)                              | N      | N    |


### Glossary

| Abbreviation     | Details                           |
| ---------------- | --------------------------------- |
| TC               | TestCase                          |
| DAO              | Data Agility Operator             |
| CSPA             | CstorPool Auto                    |
| OO               | OpenEBS Operator                  |
