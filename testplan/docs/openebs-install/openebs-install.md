---
id: openebs-install
title: OpenEBS Install
sidebar_label: Test Strategy
---
------

## OpenEBS
As a DevOps admin, I want to deploy OpenEBS in a Kubernetes native way. I would like to deploy OpenEBS on nodes that are meant to serve storage. I want to be notified if any particular node or the entire cluster is not capable of deploying & running OpenEBS. I want OpenEBS to discover all the storage disks that it can consume in order to expose them as kubernetes persistent volumes. I want OpenEBS to provide recommendations in selecting disks that ensure data availability in-case of disk as well as node failures.

This page captures the test strategies for OpenEBS operations related to:
- Install


### OpenEBS install related test case IDs

| TCID                                                                                      |
| ----------------------------------------------------------------------------------------  |
| [TCID-DIR-OP-INSTALL-OPENEBS](TCID-DIR-OP-INSTALL-OPENEBS)                                |
| [TCID-DIR-OP-INSTALL-OPENEBS-LIMIT-RESOURCE](TCID-DIR-OP-INSTALL-OPENEBS-LIMIT-RESOURCE)  |
| [TCID-DIR-OP-RE-INSTALL-OPENEBS](TCID-DIR-OP-RE-INSTALL-OPENEBS)                          |
| [TCID-DIR-OP-INSTALL-OPENEBS-DP-ON-SPECIFIC-NODE](TCID-DIR-OP-INSTALL-OPENEBS-DP-ON-SPECIFIC-NODE)|
| [TCID-DIR-OP-INSTALL-OPENEBS-CP-ON-SPECIFIC-NODE](TCID-DIR-OP-INSTALL-OPENEBS-CP-ON-SPECIFIC-NODE)|

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

## Glossary

| Abbreviation     | Details                           |
| ---------------- | --------------------------------- |
| TCID             | TestCase ID                       |
| DIR              | Director                          |
| OP               | OPENEBS PROVISIONER               |