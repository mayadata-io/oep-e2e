---
id: OpenEBS-Enterprise 
title: OpenEBS Enterprise
sidebar_label: Test Strategy
---
------

## OpenEBS EE (OpenEBS Enterprise)

OpenEBS EE is an Enterprise version of OpenEBS certified by MayaData. This goes through rigorous testing in-addition to the testing covered as part of community edition <a href="http://openebs.ci/" target="_blank">openebs.ci</a> 

This section covers the test strategy of the OpenEBS EE component in OEP.

- Install and Upgrade - Install and upgrade of OpenEBS can be done in the following ways
  - Helm
  - Director - Testing of Install and Upgrade is covered in [Director](/docs/director/openebs-provisioning/plan) 
- Provisioning - Provisioning of Storage Engines can be done in the following ways
  - Yaml Spec
  - Director - Testing of provisioning via Director is covered in [Director](/docs/director/openebs-provisioning/plan) 
- Storage Engines - OpenEBS Supports multiple storage engines as listed below
  - cStor
  - Local PV Hostpath
  - Local PV Device
  - Jiva
  - ZFS on Local PV
  - MayaStor
- Soak Testing - These tests are performed on the Kubernetes cluster( aka Workload Cluster) which has 10 worker nodes. Workload cluster has been deployed with various stateful applications, each of the workloads consumes different recommended OpenEBS storage engine. This setup will be continuously run with certain pre-defined load.  The following tests would be performed on the cluster post upgrade of every build
  - Provisioning and de-provisioning of storage will be performed to find any deviation. 
  - Day2 operations will be performed on live cluster.
  - Storage chaos would be performed to verify the application resiliency. 

| Workload          | Storage Engine    | Type | Replicas | Replication Type        |
| ----------------- | ----------------- | ---- | -------- | ----------------------- |
| Kafka             | Local PV Hostpath | RWO  | 3        | Application Replication |
| Cassandra         | Local PV Device   | RWO  | 3        | Application Replication |
| MySQL             | cStor             | RWO  | 3        | Storage Replication     |
| Percona           | Jiva              | RWO  | 3        | Storage Replication     |
| Wordpress (NFS)   | cStor             | RWX  | 3        | Storage Replication     |
| Wordpress (NFS)   | Jiva              | RWX  | 3        | Storage Replication     |
| NGNIX (Webserver) | cStor             | ROX  | 3        | Storage Replication     |



- Security Testing - Security scan will be performed on each build 

  

- Performance - Performance will be measured against each build, there can’t be deviation of 10% with prior build.

- Reliability - Various workloads of read write operation on storage i.e 100:0RW, 20:80RW, 30:70RW, 50:50RW, 30:70RW, 0:100RW FIO/vdbench test will be performed on a build with minimum of 72 hours before any monthly release.

- Scalability -  **TODO**






