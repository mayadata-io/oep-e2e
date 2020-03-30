---
id: gitlabstages
title: E2E Pipelines
sidebar_label: Pipelines
---
------

## GitLab

OEP E2E is done using GitLab. Each PR in any of the Director Repositories or DAO Respositories will trigger a set of E2E piplines. It is also possible to trigger the pipelines manually. 

### Director Repositories

Following repositories will have gitlab-ci.yml files which will trigger pipelines in [oep-e2e-gcp](https://github.com/mayadata-io/oep-e2e-gcp), [oep-e2e-konvoy](https://github.com/mayadata-io/oep-e2e-konvoy) and [oep-e2e-rancher](https://github.com/mayadata-io/oep-e2e-rancher) repositories.



Maya-io-server, maya-ui, maya-chatops, openebs-manager, dmaas-agent etc. 



### DAO Repositories

Following repositories will have gitlab-ci.yml files which will trigger pipelines in [oep-e2e-gcp](https://github.com/mayadata-io/oep-e2e-gcp), [oep-e2e-konvoy](https://github.com/mayadata-io/oep-e2e-konvoy) and [oep-e2e-rancher](https://github.com/mayadata-io/oep-e2e-rancher) repositories.

[cstorpoolauto](https://github.com/mayadata-io/cstorpoolauto) and [storage-provisioner](https://github.com/mayadata-io/storage-provisioner).

## GitLab Stages

Following are the suggested stages for each pipeline.

**Cluster setup**

Setup the cluster, underlying disks, networks or any pre-requisites that need to be done. This is not counted as a test case and hence is not calculated for coverage.

**Director Install and upgrade**

Director installation test cases, upgrade cases, day 2 operations of director, chaos tests around director are done in this stage.

**Functional testing with Rest**

There are a set of tests that are written against REST api. All functional, scalable and chaos testing written using these APIs will be under this stage. A separate user cluster or many user clusters are connected to Director for the tests under this stage.

**Functional testing with Selenium**

All the tests written using GUI automation or Selenium will be under this stage. A separate user cluster or many user clusters are connected to Director for the tests under this stage.

**Cluster tear down**

E2E metrics, finalizing the tests, disconnect the user clusters,clean up resources, delete Director OnPrem and scaledown/destroy cluster where DOP is installed.

