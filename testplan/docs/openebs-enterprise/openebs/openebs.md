---
id: openebs
title: OpenEBS Enterprise
sidebar_label: Test Strategy
---
------

## OpenEBS Enterprise Test Plans

OpenEBS Enterprise Edition is the enterprise version of the CNCF project OpenEBS. This enterprise edition is certified by [MayaData](https://mayadata.io/). This is one of the components offered in OpenEBS Enterprise Platform _(OEP)_.

This section provides **test plans** for OpenEBS enterprise edition builds. It adds production usecases as part of its test strategies in addition to the ones covered in community edition i.e. <a href="http://openebs.ci/" target="_blank">openebs.ci</a> 

### TC-OO-EE-HELM
As a DevOps admin, I rely on my CI CD & HELM to manage all of my kubernetes specifications. I would like to do the same to manage storage specifications.

#### TC-OO-EE-HELM-INSTALL
As a DevOps admin, I want to install openebs enterprise on my kubernetes cluster via helm. This should install openebs with required specifications & necessary tunables to run openebs on my kubernetes cluster. Over a period of time, I would like to modify the helm based tunables based on my cluster needs. I should be notified via kubernetes custom resources if openebs running in my cluster uses deprecated, invalid or wrong tunables.

#### TC-OO-EE-HELM-UPGRADE
As a DevOps admin, I want to upgrade openebs enterprise on my kubernetes cluster via helm. This should upgrade openebs with required specifications & necessary tunables to continue running openebs on my kubernetes cluster. All of the previous helm values that were modified by me should not get overridden. However, old defaults should be overriden with new defaults. Newly added tunables should get applied over corresponding openebs components. I should be notified via kubernetes custom resources if openebs running in my cluster uses deprecated, invalid or non-performing tunables.

#### Test Case IDs -- Based on HELM

| TCID                                                         | GCP    | KONVOY |
| ------------------------------------------------------------ | ------ | ------ |
| [TC-OO-EE-HELM-INSTALL](TC-OO-EE-HELM-INSTALL)               |        |        |
| [TC-OO-EE-HELM-UPGRADE](TC-OO-EE-HELM-UPGRADE)               |        |        |

### TC-OO-SCALE
As a DevOps admin, I would like to run scalability tests against openebs on my kubernetes cluster. I would like to ensure following steps to be executed to mark this scalability test as a success:
- Tests to be performed on a Kubernetes workload cluster with a minimum of **10** nodes
- Workload cluster will have deployments of various stateful applications
- Each application will consume OpenEBS storage engine that suits the most
- There will be a minimum of 10 separate application instances running on different namespaces
- OpenEBS upgrades to be performed to bring all openebs volumes to latest stable version 
- Following tests are performed on the cluster post OpenEBS upgrade:
    - Run health checks on existing applications
    - Run health checks on volumes consumed by these applications
    - Provision and de-provision new/existing applications to find issues if any
    - Run several day 2 operations
    - Run storage chaos to verify application resiliency

Below is a tabular representation of above testplan:

| Workload          | Storage Engine    | Type | Replicas | Replication  | Instances |
| ----------------- | ----------------- | ---- | -------- | -------------|---------- |
| Kafka             | Local PV Hostpath | RWO  | 3        | Application  |  10       |
| Cassandra         | Local PV Device   | RWO  | 3        | Application  |  10       |
| MySQL             | cStor             | RWO  | 3        | Storage      |  10       |
| Percona           | Jiva              | RWO  | 3        | Storage      |  10       |
| Wordpress (NFS)   | cStor             | RWX  | 3        | Storage      |  10       |
| Wordpress (NFS)   | Jiva              | RWX  | 3        | Storage      |  10       |
| NGNIX (Webserver) | cStor             | ROX  | 3        | Storage      |  10       |

#### Test Case IDs -- Based on Scale

| TCID                                                               | GCP    | KONVOY |
| ------------------------------------------------------------------ | ------ | ------ |
| [TC-OO-EE-SCALE-KAFKA](TC-OO-EE-SCALE-KAFKA)                       |        |        |
| [TC-OO-EE-SCALE-CASSANDRA](TC-OO-EE-SCALE-CASSANDRA)               |        |        |
| [TC-OO-EE-SCALE-MYSQL](TC-OO-EE-SCALE-MYSQL)                       |        |        |
| [TC-OO-EE-SCALE-PERCONA](TC-OO-EE-SCALE-PERCONA)                   |        |        |
| [TC-OO-EE-SCALE-WORDPRESS-CSTOR](TC-OO-EE-SCALE-WORDPRESS-CSTOR)   |        |        |
| [TC-OO-EE-SCALE-WORDPRESS-JIVA](TC-OO-EE-SCALE-WORDPRESS-JIVA)     |        |        |
| [TC-OO-EE-SCALE-WORDPRESS-NGINX](TC-OO-EE-SCALE-WORDPRESS-NGINX)   |        |        |


### Security Test Plan
**TODO**

### Soak Test Plan 
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

