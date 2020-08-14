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

| TCID                                                                                      | Cluster   |
| ----------------------------------------------------------------------------------------  |-----------|
| [TCID-DIR-OP-INSTALL-OPENEBS](TCID-DIR-OP-INSTALL-OPENEBS)                                |    C2     |
| [TCID-DIR-OP-INSTALL-OPENEBS-LIMIT-RESOURCE](TCID-DIR-OP-INSTALL-OPENEBS-LIMIT-RESOURCE)  |    C3     |
| [TCID-DIR-OP-RE-INSTALL-OPENEBS](TCID-DIR-OP-RE-INSTALL-OPENEBS)                          |    C3     |
| [TCID-DIR-OP-INSTALL-OPENEBS-DP-ON-SPECIFIC-NODE](TCID-DIR-OP-INSTALL-OPENEBS-DP-ON-SPECIFIC-NODE)|C3 |
| [TCID-DIR-OP-INSTALL-OPENEBS-CP-ON-SPECIFIC-NODE](TCID-DIR-OP-INSTALL-OPENEBS-CP-ON-SPECIFIC-NODE)|C3 |



## Glossary

| Abbreviation     | Details                           |
| ---------------- | --------------------------------- |
| TCID             | TestCase ID                       |
| DIR              | Director                          |
| OP               | OPENEBS PROVISIONER               |
| C2               | CLUSTER-2                         |
| C3               | CLUSTER-3                         |
