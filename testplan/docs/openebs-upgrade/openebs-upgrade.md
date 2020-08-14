---
id: openebs-upgrade
title: OpenEBS Upgrade
sidebar_label: Test Strategy
---
------

## OpenEBS Upgrade
As a DevOps admin, I want to deploy OpenEBS in a Kubernetes native way. I would like to deploy OpenEBS on nodes that are meant to serve storage. I want to be notified if any particular node or the entire cluster is not capable of deploying & running OpenEBS. I want OpenEBS to discover all the storage disks that it can consume in order to expose them as kubernetes persistent volumes. I want to upgrade OpenEBS to latest versions.

This page captures the test strategies for OpenEBS operations related to:
- OpenEBS upgrade test cases w.r.t control plane components
- OpenEBS upgrade test cases w.r.t CStor
- openEBS Upgrade test cases w.r.t Jiva

### OpenEBS upgrade test cases w.r.t control plane component

| TCID                                                                                       | Cluster |
| ------------------------------------------------------------------------------------------ |---------|
| [TCID-DIR-OP-OPENEBS-UPGRADE-CP](TCID-DIR-OP-OPENEBS-UPGRADE-CP)                           |   C3    |



### OpenEBS upgrade test cases w.r.t CStor

| TCID                                                                                       |
| ------------------------------------------------------------------------------------------ |
| [TCID-DIR-OP-UPGRADE-CSTOR-POOL](TCID-DIR-OP-UPGRADE-CSTOR-POOL)                           |
| [TCID-DIR-OP-UPGRADE-CSTOR-VOLUME](TCID-DIR-OP-UPGRADE-CSTOR-VOLUME)                       |
| [TCID-DIR-OP-UPGRADE-CSTOR-POOL-ALL-PODS-RUNNING](TCID-DIR-OP-UPGRADE-CSTOR-POOL-ALL-PODS-RUNNING)|
| [TCID-DIR-OP-UPGRADE-CSTOR-POOL-ONE-POD-PENDING](TCID-DIR-OP-UPGRADE-CSTOR-POOL-ONE-POD-PENDING)|
| [TCID-DIR-OP-UPGRADE-CSTOR-POOL-ALL-PODS-PENDING](TCID-DIR-OP-UPGRADE-CSTOR-POOL-ALL-PODS-PENDING)|


### Upgrade test cases w.r.t Jiva

| TCID                                                                                       |
| ------------------------------------------------------------------------------------------ |
| [TCID-DIR-OP-UPGRADE-JIVA-VOLUME](TCID-DIR-OP-UPGRADE-JIVA-VOLUME)                         |
| [TCID-DIR-OP-UPGRADE-JIVA-VOLUME-ONE-REPLICA-PENDING](TCID-DIR-OP-UPGRADE-JIVA-VOLUME-ONE-REPLICA-PENDING)|
| [TCID-DIR-OP-UPGRADE-JIVA-VOLUME-ALL-REPLICAS-PENDING](TCID-DIR-OP-UPGRADE-JIVA-VOLUME-ALL-REPLICAS-PENDING)|
| [TCID-DIR-OP-UPGRADE-JIVA-VOLUME-TWO-REPLICAS-PENDING](TCID-DIR-OP-UPGRADE-JIVA-VOLUME-TWO-REPLICAS-PENDING)|

---
**NOTE**

- C1 would be installed with latest version of DOP
- C2 and C3 are connected to C1 using DOP APIs
---

## Glossary

| Abbreviation     | Details                           |
| ---------------- | --------------------------------- |
| TCID             | TestCase ID                       |
| DIR              | Director                          |
| OP               | OPENEBS PROVISIONER               |
| C1               | CLUSTER-1                         |
| C2               | CLUSTER-2                         |
| C3               | CLUSTER-3                         |