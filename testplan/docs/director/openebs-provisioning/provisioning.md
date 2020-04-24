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


###  OpenEBS Install

- [TCID-DIR-OP-BD-VIEW-ALL](TCID-DIR-OP-BD-VIEW-ALL) - View all devices of a kubernetes cluster
- [TCID-DIR-OP-BD-VIEW-SCALE](TCID-DIR-OP-BD-VIEW-SCALE) - View all devices on a scaled kubernetes cluster
- [TCID-DIR-OP-BD-VIEW-SCALE-RESTART](TCID-DIR-OP-BD-VIEW-SCALE-RESTART) - View all devices on a scaled kubernetes cluster even after multiple restarts of this cluster is observed
- [TCID-DIR-OP-BD-FILTER-SSD](TCID-DIR-OP-BD-FILTER-SSD) - View all SSD based devices of a kubernetes cluster
- [TCID-DIR-OP-BD-FILTER-PATH](TCID-DIR-OP-BD-FILTER-PATH) - View devices with specific path across the kubernetes cluster
- [TCID-DIR-OP-BD-IGNORE](TCID-DIR-OP-BD-IGNORE) - Avoid devices from specific nodes of a kubernetes cluster
- [TCID-DIR-OP-BD-VIEW-TOGGLE](TCID-DIR-OP-BD-VIEW-TOGGLE) - Toggle viewing devices from specific nodes of a kubernetes cluster


###  OpenEBS Control Plane Upgrade


### OpenEBS Data Plane Upgrade


### CStor Pool Recommendations 
- [TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST) List all cstor pool recommendations
- [TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-NO-NDM](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-NO-NDM)  List all cstor pool recommendations with NDM not running
- [TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-STRIPE](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-STRIPE) List all stripe cstor pool recommendations
- [TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-MIRROR](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-MIRROR) List all mirror cstor pool recommendations
- [TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-MIRROR](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-MIRROR) Create mirror cstor pool cluster
- [TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-STRIPE](TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-STRIPE) Create stripe cstor pool cluster


### Jiva Pool Provisioning 


###  Storage Class Provisioning

- cStor
- Jiva
- Local PV Hostpath
- Local PV Device

###  Volume  Provisioning

- cStor
- Jiva
- Local PV Hostpath
- Local PV Device


- [TCID-DIR-OP-JIVA-HEALTH-RESTART](TCID-DIR-OP-JIVA-HEALTH-RESTART) Jiva volumes should run even after multiple restarts of the kubernetes cluster is observed


## Glossary

| Abbreviation     | Details                           |
| ---------------- | --------------------------------- |
| TCID             | TestCase ID                       |
| DIR              | Director                          |
