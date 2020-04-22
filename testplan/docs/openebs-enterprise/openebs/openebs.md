---
id: openebs
title: OpenEBS Enterprise
sidebar_label: Test Strategy
---
------

## OpenEBS Enterprise Test Plans

OpenEBS Enterprise Edition is the enterprise version of the CNCF project OpenEBS. This enterprise edition is certified by [MayaData](https://mayadata.io/). This is one of the components offered in OpenEBS Enterprise Platform _(OEP)_.

This section provides **test plans** for OpenEBS enterprise edition builds. It adds production usecases as part of its test strategies in addition to the ones covered in community edition i.e. <a href="http://openebs.ci/" target="_blank">openebs.ci</a> 

### TC-OEE-OO-HELM
As a DevOps admin, I rely on my CI CD & HELM to manage all of my kubernetes specifications. I would like to do the same to manage storage specifications.

#### TC-OEE-OO-HELM-INSTALL
As a DevOps admin, I want to install openebs enterprise on my kubernetes cluster via helm. This should install openebs with required specifications & necessary tunables to run openebs on my kubernetes cluster. Over a period of time, I would like to modify the helm based tunables based on my cluster needs. I should be notified via kubernetes custom resources if openebs running in my cluster uses deprecated, invalid or wrong tunables.

#### TC-OEE-OO-HELM-UPGRADE
As a DevOps admin, I want to upgrade openebs enterprise on my kubernetes cluster via helm. This should upgrade openebs with required specifications & necessary tunables to continue running openebs on my kubernetes cluster. All of the previous helm values that were modified by me should not get overridden. However, old defaults should be overriden with new defaults. Newly added tunables should get applied over corresponding openebs components. I should be notified via kubernetes custom resources if openebs running in my cluster uses deprecated, invalid or non-performing tunables.

#### Test Case IDs -- Based on HELM

| TCID                                                         | GCP    | KONVOY |
| ------------------------------------------------------------ | ------ | ------ |
| [TC-OEE-OO-HELM-INSTALL](TC-OEE-OO-HELM-INSTALL)             |        |        |
| [TC-OEE-OO-HELM-UPGRADE](TC-OEE-OO-HELM-UPGRADE)             |        |        |

### TC-OEE-SOAK
As a DevOps admin, I would like to run soak tests against openebs on my kubernetes cluster. I would like to ensure following steps to be executed to mark soak tests as a success:

- Tests to be performed on a Kubernetes **workload** cluster
- This workload cluster should have a minimum of **10** nodes
- Workload cluster will have deployments of various stateful applications
- Each application will consume OpenEBS storage engine that suits the most
- These applications are **never** brought down
- There will be a minimum of **10 application instances** 
    - Each instance will be running on its own namespace
- Upgrades to be performed to latest stable builds
    - Upgrades will be triggered only after due approvals
    - Upgrade can either be w.r.t kubernetes or openebs or both
- Following checks are performed continuously:
    - Run health checks on existing applications
    - Run health checks on volumes consumed by these applications
- Following sanity tests to be performed continuously:
    - Provision new applications to find issues if any
    - De-provision these new applications to find issues if any
- Following Day 2 operations to be performed at regular intervals:
    - TODO
- Following Chaos operations to be performed at regular intervals:
    - TODO

#### Tabular representation

| Workload          | Storage Engine    | Type | Replicas | Replication  | Instances |
| ----------------- | ----------------- | ---- | -------- | -------------|---------- |
| Kafka             | Local PV Hostpath | RWO  | 3        | Application  |  10       |
| Cassandra         | Local PV Device   | RWO  | 3        | Application  |  10       |
| MySQL             | cStor             | RWO  | 3        | Storage      |  10       |
| Percona           | Jiva              | RWO  | 3        | Storage      |  10       |
| Wordpress (NFS)   | cStor             | RWX  | 3        | Storage      |  10       |
| Wordpress (NFS)   | Jiva              | RWX  | 3        | Storage      |  10       |
| NGNIX (Webserver) | cStor             | ROX  | 3        | Storage      |  10       |

#### Test Case IDs

| TCID                                                               | GCP    | KONVOY |
| ------------------------------------------------------------------ | ------ | ------ |
| [TC-OEE-SOAK-KAFKA](TC-OEE-SOAK-KAFKA)                             |        |        |
| [TC-OEE-SOAK-CASSANDRA](TC-OEE-SOAK-CASSANDRA)                     |        |        |
| [TC-OEE-SOAK-MYSQL](TC-OEE-SOAK-MYSQL)                             |        |        |
| [TC-OEE-SOAK-PERCONA](TC-OEE-SOAK-PERCONA)                         |        |        |
| [TC-OEE-SOAK-WORDPRESS-CSTOR](TC-OEE-SOAK-WORDPRESS-CSTOR)         |        |        |
| [TC-OEE-SOAK-WORDPRESS-JIVA](TC-OEE-SOAK-WORDPRESS-JIVA)           |        |        |
| [TC-OEE-SOAK-WORDPRESS-NGINX](TC-OEE-SOAK-WORDPRESS-NGINX)         |        |        |


### Scalability Test Plans
As a DevOps admin, I would like to run scalability tests against openebs on my kubernetes cluster. I would like to ensure following steps to be executed to mark scalability tests as a success:

- Tests to be performed on kubernetes cluster with enough resources
- Tests will involve ramping up of stateful applications consuming openebs volumes
    - Applications will be ramped up from **0** till **200**
    - Ramp count can be 10 i.e. 10 applications will be created simultaneously
    - Application specific loads will be run against each for 60 minutes
    - Creation metrics will be captured
    - Application metrics will be captured
    - Volume metrics will be captured
    - Deviation of metrics will be reported as warnings or errors
- Tests will involve ramping down of these stateful applications
    - Number of applications will be ramped down from 200 to 0
    - Ramp down count can be 10 i.e. 10 applications will be deleted simultaneously
    - Deletion metrics will be captured
    - Application metrics will be captured
    - Volume metrics will be captured
    - Deviation of metrics will be reported as warnings or errors

#### Tabular representation

| Workload          | Storage Engine    | Type | Replicas | Min  | Max |
| ----------------- | ----------------- | ---- | -------- | ---- | --- |
| Kafka             | Local PV Hostpath | RWO  | 3        | 0    | 200 |
| Kafka             | Local ZFS         | RWO  | 3        | 0    | 200 |
| Cassandra         | Local PV Device   | RWO  | 3        | 0    | 200 |
| Cassandra         | Local ZFS         | RWO  | 3        | 0    | 200 |
| MySQL             | cStor             | RWO  | 3        | 0    | 200 |
| Percona           | Jiva              | RWO  | 3        | 0    | 200 |
| Wordpress (NFS)   | cStor             | RWX  | 3        | 0    | 200 |
| Wordpress (NFS)   | Jiva              | RWX  | 3        | 0    | 200 |
| NGNIX (Webserver) | cStor             | ROX  | 3        | 0    | 200 |

#### References

- https://github.com/openebs/zfs-localpv/labels/scalability

#### Test Case IDs

| TCID                                                               | GCP    | KONVOY |
| ------------------------------------------------------------------ | ------ | ------ |
| [TC-OEE-SCALE-KAFKA](TC-OEE-SCALE-KAFKA)                           |        |        |
| [TC-OEE-SCALE-CASSANDRA](TC-OEE-SCALE-CASSANDRA)                   |        |        |
| [TC-OEE-SCALE-MYSQL](TC-OEE-SCALE-MYSQL)                           |        |        |
| [TC-OEE-SCALE-PERCONA](TC-OEE-SCALE-PERCONA)                       |        |        |
| [TC-OEE-SCALE-WORDPRESS-CSTOR](TC-OEE-SCALE-WORDPRESS-CSTOR)       |        |        |
| [TC-OEE-SCALE-WORDPRESS-JIVA](TC-OEE-SCALE-WORDPRESS-JIVA)         |        |        |
| [TC-OEE-SCALE-WORDPRESS-NGINX](TC-OEE-SCALE-WORDPRESS-NGINX)       |        |        |


### Security Test Plans
**TODO**


## Test Criteria
- Performance will be measured against each build
    - 10% deviation or more makes the release risky
- Simulate workloads with varying READ WRITE percentage against storage 
    - e.g. 100:0RW, 20:80RW, 30:70RW, 50:50RW, 30:70RW, 0:100RW
- Run test load for a minimum of 72 hours


### Glossary

| Abbreviation     | Details                                                        |
| ---------------- | -------------------------------------------------------------- |
| TC               | TestCase                                                       |
| WORKLOAD         | A kubernetes cluster that runs continuously                    |
| OEE              | OpenEBS Enterprise Edition                                     |
| OO               | OpenEBS Operator                                               |

