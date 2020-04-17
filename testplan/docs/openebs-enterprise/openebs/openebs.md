---
id: openebs
title: OpenEBS Enterprise
sidebar_label: Test Strategy
---
------

## OpenEBS EE (OpenEBS Enterprise)

OpenEBS EE is the enterprise version of the CNCF project OpenEBS. This enterprise edition is certified by [MayaData](https://mayadata.io/). This is one of the components offered in OpenEBS Enterprise Platform _(OEP)_.

This section provides **test plans** for OpenEBS enterprise edition builds. It adds production usecases as part of its test strategies in addition to the ones covered in community edition i.e. <a href="http://openebs.ci/" target="_blank">openebs.ci</a> 

### Sanity Test Plans
- OpenEBS install
    - Helm (via DAO)
    - [Director](/docs/director/openebs-provisioning/plan)
- OpenEBS upgrade
    - Helm (via DAO)
    - [Director](/docs/director/openebs-provisioning/plan)
- Provisioning of applications using various OpenEBS storage engines
    - DAO
    - [Director](/docs/director/openebs-provisioning/plan) 


### Scalability Test Plans
- These tests are performed on a Kubernetes cluster with a minimum of **10** nodes
    - This cluster is also known as _Workload cluster_
- Workload cluster will have deployments of various stateful applications
- Each workload application will consume OpenEBS storage engine that suits the most
- Following tests are performed on the cluster post OpenEBS upgrade
    - Run health checks on existing applications
    - Provision and de-provision applications to find any deviation
    - Several day2 operations
    - Storage chaos to verify the application resiliency

Below is a tabular representation of above testplan:

| Workload          | Storage Engine    | Type | Replicas | Replication  | Instances |
| ----------------- | ----------------- | ---- | -------- | ------------------------ |
| Kafka             | Local PV Hostpath | RWO  | 3        | Application  |  10       |
| Cassandra         | Local PV Device   | RWO  | 3        | Application  |  10       |
| MySQL             | cStor             | RWO  | 3        | Storage      |  10       |
| Percona           | Jiva              | RWO  | 3        | Storage      |  10       |
| Wordpress (NFS)   | cStor             | RWX  | 3        | Storage      |  10       |
| Wordpress (NFS)   | Jiva              | RWX  | 3        | Storage      |  10       |
| NGNIX (Webserver) | cStor             | ROX  | 3        | Storage      |  10       |


### Security Test Plan
**TODO**

### Soak Test Plan 
**TODO**

## Test Criteria
- Performance will be measured against each build
    - 10% deviation or more makes the release risky
- Reliability
    - Simulate workloads with varying READ WRITE percentage against storage 
    - e.g. 100:0RW, 20:80RW, 30:70RW, 50:50RW, 30:70RW, 0:100RW FIO/vdbench tests
    - Run for a minimum of 72 hours


### Glossary
- Following are the list of supported OpenEBS storage engines
    - cStor
    - Local PV Hostpath
    - Local PV Device
    - Jiva
    - ZFS on Local PV
    - MayaStor



