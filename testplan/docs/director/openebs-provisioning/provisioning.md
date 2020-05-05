---
id: provisioning
title: OpenEBS Install, Upgrade & Provisioning
sidebar_label: Test Strategy
---
------

## OpenEBS
As a DevOps admin, I want to deploy OpenEBS in a Kubernetes native way. I would like to deploy OpenEBS on nodes that are meant to serve storage. I want to be notified if any particular node or the entire cluster is not capable of deploying & running OpenEBS. I want OpenEBS to discover all the storage disks that it can consume in order to expose them as kubernetes persistent volumes. I want OpenEBS to provide recommendations in selecting disks that ensure data availability in-case of disk as well as node failures.

This page captures the test strategies for OpenEBS operations related to:
- Install
- Upgrade
- Pool Provisioning
- Volume Provisioning 


###  TCID-DIR-OP-DEVICE-VIEW
As a DevOps admin, I want OpenEBS to provide me all the storage disks that are eligible to be consumed by applications. OpenEBS should provide the list of disks that spans across nodes within the cluster. It is expected that during the lifetime of this cluster, few node restarts, upgrading this cluster to newer versions will be observed / performed. OpenEBS should continue to provide me storage information like the Day 0 days.

| TCID                                                                          |
| ------------------------------------------------------------------------------|
| [TCID-DIR-OP-DEVICE-VIEW-ALL](TCID-DIR-OP-DEVICE-VIEW-ALL)                    |
| [TCID-DIR-OP-DEVICE-VIEW-SCALE](TCID-DIR-OP-DEVICE-VIEW-SCALE)                |
| [TCID-DIR-OP-DEVICE-VIEW-SCALE-RESTART](TCID-DIR-OP-DEVICE-VIEW-SCALE-RESTART)|

### TCID-DIR-OP-DEVICE-FILTER
As a DevOps admin, I want to mark certain devices for consumption by OpenEBS. I want OpenEBS to avoid using devices that are not meant for the former. This should help me & my teams to use storage by avoiding the noisy neighbour problem. In some of the cases, I want OpenEBS to avoid using specific nodes during initial days. However, I should have the flexibility to add & remove these nodes for OpenEBS consumption based on load experienced by the cluster.

| TCID                                                                   |
| ---------------------------------------------------------------------- |
| [TCID-DIR-OP-DEVICE-FILTER-SSD](TCID-DIR-OP-DEVICE-FILTER-SSD)         |
| [TCID-DIR-OP-DEVICE-FILTER-PATH](TCID-DIR-OP-DEVICE-FILTER-PATH)       |
| [TCID-DIR-OP-DEVICE-IGNORE-NODE](TCID-DIR-OP-DEVICE-IGNORE-NODE)       |
| [TCID-DIR-OP-DEVICE-TOGGLE-NODE](TCID-DIR-OP-DEVICE-TOGGLE-NODE)       |


### TCID-DIR-OP-CONTROL-PLANE-UPGRADE


### TCID-DIR-OP-DATA-PLANE-UPGRADE


### TCID-DIR-OP-CSTOR-POOL
As a DevOps admin, I want to run applications on a storage that supports replication & snapshots. I want to get recommendations on storage pool plans that can help the applications recover from disk as well as node failures. Since openebs cstor supports my use cases, I would like to get cstor pool related recommendations that helps design pools that are resilient to node & disk failures.

| TCID                                                                                       |
| ------------------------------------------------------------------------------------------ |
|[TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST)              |
|[TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-STRIPE](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-STRIPE)|
|[TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-MIRROR](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-MIRROR)|
|[TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-MIRROR](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-MIRROR)|
|[TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-STRIPE](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-STRIPE)|

### TCID-DIR-OP-CSTOR-POOL-DAY2 
As a DevOps admin, I manage multiple stateful applications on cstor storage pool. There are instances where disks that form these pools turn bad. In such scenarios, I want to replace these disks with newer ones. In addition, there will be periodic demands to supplement additional storage capacity on the account of pool getting filled up. I want cstor pool should provide capability to add storage capacity to existing pools. It will be great to let cstor pool operator notify me of above issues as well. I should be notified of the number of disks that has gone bad, the percentage of pool capacity used versus remaining, the pools that are performing well versus those that do not.

| TCID                                                                                       |
| ------------------------------------------------------------------------------------------ |
|[TCID-DIR-OP-CSTOR-POOL-DAY2-REPLACE-BAD-DISK](TCID-DIR-OP-CSTOR-POOL-DAY2-REPLACE-BAD-DISK)|
|[TCID-DIR-OP-CSTOR-POOL-DAY2-ADD-DISK](TCID-DIR-OP-CSTOR-POOL-DAY2-ADD-DISK)                |


| TCID                                                                                       |
| ------------------------------------------------------------------------------------------ |
|[TCID-DIR-OP-CSTOR-POOL-DAY2-NOTIFY-BAD-DISK](TCID-DIR-OP-CSTOR-POOL-DAY2-NOTIFY-BAD-DISK)  |
|[TCID-DIR-OP-CSTOR-POOL-DAY2-NOTIFY-POOL-CAP](TCID-DIR-OP-CSTOR-POOL-DAY2-NOTIFY-POOL-CAP)  |
|[TCID-DIR-OP-CSTOR-POOL-DAY2-NOTIFY-POOL-PERF](TCID-DIR-OP-CSTOR-POOL-DAY2-NOTIFY-POOL-PERF)|


### TCID-DIR-OP-CSTOR-POOL-DAY2-VOL-RE-BALANCE
As a DevOps admin, I manage multiple stateful applications on one or more cstor storage pools. There will be instances where I want to re-balance these applications to pool instances with more available storage capacity or those pool instances that perform better. In other cases, I want to move some or all applications from one given storage pool to another storage pool in the same cluster.

| TCID                                                                                       |
| ------------------------------------------------------------------------------------------ |
|[TCID-DIR-OP-CSTOR-POOL-DAY2-VOL-RE-BALANCE](TCID-DIR-OP-CSTOR-POOL-DAY2-VOL-RE-BALANCE)    |


### TCID-DIR-OP-CSTOR-POOL-RESTARTS 
As a DevOps admin, I want to run applications on a storage that supports replication & snapshots. I want to get recommendations on storage pool plans that can help the applications recover from disk as well as node failures. Since openebs cstor supports my use cases, I would like to verify cstor pools with node restarts, node upgrades, openebs pod evictions, node replacements scenarios.


| TCID                                                                                       |
| ------------------------------------------------------------------------------------------ |
|[TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-NO-NDM](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-NO-NDM)|
|[TCID-DIR-OP-CSTOR-POOL-RECOMMEND-MIRROR-UPGRADE-NODE](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-MIRROR-UPGRADE-NODE)    |
|[TCID-DIR-OP-CSTOR-POOL-RECOMMEND-MIRROR-REBOOT-NODE](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-MIRROR-REBOOT-NODE)      |
|[TCID-DIR-OP-CSTOR-POOL-RECOMMEND-RAIDZ-UPGRADE-NODE](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-RAIDZ-UPGRADE-NODE)      |
|[TCID-DIR-OP-CSTOR-POOL-RECOMMEND-RAIDZ-REBOOT-NODE](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-RAIDZ-REBOOT-NODE)        |


### TCID-DIR-OP-CSTOR-VOLUME

### TCID-DIR-OP-JIVA-VOLUME

### TCID-DIR-OP-LOCAL-HOSTPATH-VOLUME

### TCID-DIR-OP-LOCAL-DEVICE-VOLUME



## Glossary

| Abbreviation     | Details                           |
| ---------------- | --------------------------------- |
| TCID             | TestCase ID                       |
| DIR              | Director                          |
| OP               | OPENEBS PROVISIONER               |