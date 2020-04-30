---
id: dmaas
title: DMaaS
sidebar_label: Test Strategy
---
------

## DMaaS

Data Management as a Service provides backup & restore options to stateful applications. Following sections describe various use cases that are required by enterprise users with respect to their business continuity plans.

### TCID-DIR-DMAAS-SOURCE-CLUSTER-GONE
As a DevOps admin, I manage statefulset applications in my kubernetes cluster. I want to have continuity plans for these applications. I want to take cloud based backup on a periodic basis & restore them when my source cluster is not available due to some unforeseen events. I should be able to restore from these backups _(somewhere in the cloud)_ to any new cluster that will be created only during these unforeseen situations.

| TCID                                                                    | Status |
| ----------------------------------------------------------------------- | ----   |
| [TCID-DIR-DMAAS-SOURCE-CLUSTER-GONE](TCID-DIR-DMAAS-SOURCE-CLUSTER-GONE)|        |

### TCID-DIR-DMAAS-VERSION-COMPATIBILITY-ML
As a ML scientist, I need to share data amongst fellow colleagues and teams to run specific learning algorithms based on the same data. These teams may be running their programs on different versions of Kubernetes and/or Director. I want to run machine learning programs without bothering about forward or backward compatibility of Kubernetes &/or Director.

| TCID                                                                              | Status |
| --------------------------------------------------------------------------------- | ----   |
| [TCID-DIR-DMAAS-VERSION-COMPATIBILITY-ML](TCID-DIR-DMAAS-VERSION-COMPATIBILITY-ML)|        |

### TCID-DIR-DMAAS-DATA-MOVEMENT-ACROSS-SETUPS
As a DevOps admin, I manage multiple clusters with each cluster dedicated to their line of business. I want backups of data from applications running on one cluster & restored to another cluster on a daily basis. _I do not want to backup the application themselves_. These clusters have different application sizing needs.

| TCID                                                                                 |Status|
| -------------------------------------------------------------------------------------  |--- |
|[TCID-DIR-DMAAS-DATA-MOVEMENT-ACROSS-SETUPS](TCID-DIR-DMAAS-DATA-MOVEMENT-ACROSS-SETUPS)|    |

### TCID-DIR-DMAAS-MYSQL
As a DevOps admin, I manage MYSQL statefulset applications. These applications have a dependency on configmap. Both application as well as configmap reside in their specific namespace. I would like to have continuity plans for these applications. I want to take backup on a periodic basis & restore them optionally to verify if these backups are valid. I would like to maintain the count of backups so that these backups donot fill up the storage. I would like to store these backups at my desired S3 location.

| TCID                                             | Status |
| ------------------------------------------------ | ----   |
| [TCID-DIR-DMAAS-MYSQL](TCID-DIR-DMAAS-MYSQL)     |        |


### TCID-DIR-DMAAS-CORTEX
As a DevOps admin, I manage cortex application. Cortex has a dependency on cassandra. I would like to have continuity plans for this application. I want to take on demand backup(s) of cortex & cassandra including their configuration & volumes. I want to restore the backup to verify before uploading the same to S3. I would like to be notified if my S3 location has enough space to accomodate new backups.

| TCID                                             | Status|
| ------------------------------------------------ | ----  |
| [TCID-DIR-DMAAS-CORTEX](TCID-DIR-DMAAS-CORTEX)   |       |


### TCID-DIR-DMAAS-PORTAL
As a DevOps admin, I manage a portal which in turn is a suite of applications that includes multiple kubernetes deployments, statefulsets, configurations, serviceaccounts, secrets, custom resources & volumes. I would like to take periodic backups of this portal except a few resources namely nginx-controller deployment & ingress resources. I want these backups to be uploaded to multiple S3 locations. As part of the business continuity plan, I want to verify particular backups on an on-demand basis by restoring this portal on a different cluster & verifying its state.

| TCID                                             | Status |
| ------------------------------------------------ |  ----  |
| [TCID-DIR-DMAAS-PORTAL](TCID-DIR-DMAAS-PORTAL)   |        |


### TCID-DIR-DMAAS-PSP
As a DevOps admin, I manage multiple kubernetes applications. I have an extensive set of PodSecurityPolicies that govern the infrastructure policies in the cluster. I would like to take periodic backups these pod security policies and upload them to S3. As part of the my need to let all kubernetes clusters follow the same governance rules, I want to restore these pod security policies across other clusters.

| TCID                                             | Status |
| ------------------------------------------------ |  ----  |
| [TCID-DIR-DMAAS-PSP](TCID-DIR-DMAAS-PSP)         |        |


### TCID-DIR-DMAAS-EXCLUDE-SECRET
As a DevOps admin, I manage multiple kubernetes clusters. Each of these clusters cater to different lines of businesses. Any particular team's role vary depending on the cluster. As part of business continuity plans that adhere to above security need, I want to exclude backing up secrets. In other words, **no** secrets should get uploaded to S3.

| TCID                                                            | Status |
| --------------------------------------------------------------- |  ----  |
| [TCID-DIR-DMAAS-EXCLUDE-SECRET](TCID-DIR-DMAAS-EXCLUDE-SECRET)  |        |


### TCID-DIR-DMAAS-SCHD
As a DevOps admin, I want Director to provide a backup & restore option for my teams to self manage their k8s application continuity plans. I would expect my teams to have the ability to configure backup & restore similar to the following steps:

- Configure Director to provide scheduled backups with mixed types
    - Schedule starts with a full backup
    - Schedule should provide next 23 backups as incremental backups
    - Schedule should run every hour
    - Schedule should perform the 2nd full backup in its 25th iteration
    - Schedule should be able to backup the stateful application running on openebs volume
    - Director should upload these backups to AWS S3
    - Director should retain the S3 backups for last 3 days
- On a separate cluster
    - Director should be able to connect to S3
    - Director should be able to discover the backups
    - Director should restore the stateful application using the oldest day's backups
    - Director should restore a new application using latest but one day's backups
    - Director should restore a new application using latest backups

_NOTE: This setup involves two workload setups_

#### TCID-DIR-DMAAS-SCHD -- Based on Storage Engines

_NOTE: These test cases can be performed on any two clusters_

| TCID                                                                                |Status|
| -------------------------------------------------------------------------------     | ---- |
|[TCID-DIR-DMAAS-SCHD-CSTOR-MINIO-BUCKET](TCID-DIR-DMAAS-SCHD-CSTOR-MINIO-BUCKET)     |      |
|[TCID-DIR-DMAAS-SCHD-CSTOR-AWS-BUCKET](TCID-DIR-DMAAS-SCHD-CSTOR-AWS-BUCKET)         |      |
|[TCID-DIR-DMAAS-SCHD-JIVA-MINIO-BUCKET](TCID-DIR-DMAAS-SCHD-JIVA-MINIO-BUCKET)       |      |
|[TCID-DIR-DMAAS-SCHD-JIVA-AWS-BUCKET](TCID-DIR-DMAAS-SCHD-JIVA-AWS-BUCKET)           |      |
|[TCID-DIR-DMAAS-SCHD-LOCAL-DEV-MINIO-BUCKET](TCID-DIR-DMAAS-SCHD-LOCAL-DEV-MINIO-BUCKET)|   |
|[TCID-DIR-DMAAS-SCHD-LOCAL-DEV-AWS-BUCKET](TCID-DIR-DMAAS-SCHD-LOCAL-DEV-AWS-BUCKET)    |   |
|[TCID-DIR-DMAAS-SCHD-LOCAL-HP-MINIO-BUCKET](TCID-DIR-DMAAS-SCHD-LOCAL-HP-MINIO-BUCKET)  |   |
|[TCID-DIR-DMAAS-SCHD-LOCAL-HP-AWS-BUCKET](TCID-DIR-DMAAS-SCHD-LOCAL-HP-AWS-BUCKET)      |   |

#### TCID-DIR-DMAAS-SCHD-SOAK -- Based on Applications

_NOTE: These test cases need to be performed on two workload clusters_

| TCID                                                                     | Status |
| ------------------------------------------------------------------------ |  ----  |
| [TCID-DIR-DMAAS-SCHD-SOAK-CASSANDRA](TCID-DIR-DMAAS-SCHD-SOAK-CASSANDRA) |        |
| [TCID-DIR-DMAAS-SCHD-SOAK-KAFKA](TCID-DIR-DMAAS-SCHD-SOAK-KAFKA)         |        | 
| [TCID-DIR-DMAAS-SCHD-SOAK-MYSQL](TCID-DIR-DMAAS-SCHD-SOAK-MYSQL)         |        | 
| [TCID-DIR-DMAAS-SCHD-SOAK-WORDPRESS](TCID-DIR-DMAAS-SCHD-SOAK-WORDPRESS) |        | 
| [TCID-DIR-DMAAS-SCHD-SOAK-NGINX](TCID-DIR-DMAAS-SCHD-SOAK-NGINX)         |        | 
| [TCID-DIR-DMAAS-SCHD-SOAK-PERCONA](TCID-DIR-DMAAS-SCHD-SOAK-PERCONA)     |        | 


### TCID-DIR-DMAAS-SCHD-SOAK-MONITOR
This strategy is a continuation of above TCID-DMAAS-SCHD test strategy. As a DevOps admin, I want to monitor the following:
- view the application continuity plans of my teams
- view the S3 usage on a per team basis
- view connectivity to backup as well as restore cluster

_NOTE: This test cases need to be performed on workload cluster_

| TCID                                                                      | Status |
| ------------------------------------------------------------------------- |  ----  |
| [TCID-DIR-DMAAS-SCHD-SOAK-MONITOR](TCID-DIR-DMAAS-SCHD-SOAK-MONITOR)      |        |

## Glossary

| Abbreviation     | Details                                           |
| ---------------- | ------------------------------------------------- |
| WORKLOAD         | A k8s cluster that runs continuously              |
| DIR              | Director                                          |
| SCHD             | Schedule                                          |
| LOCAL DEV        | Local Device operator                             |
| LOCAL HP         | Local HostPath operator                           |
