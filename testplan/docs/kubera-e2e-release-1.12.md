---
id: kubera-e2e-release-1-12
title: Kubera E2E Release 1.12
sidebar_label: Kubera E2E 1.12
---

## RELEASE NOTES
This is the third release of Kubera end to end (E2E) pipelines. Team continued their focus on stabilising the pipelines. In addition the same team was busy verifying new Kubera features. Needless to say E2E was successful in finding lot of bugs given the state of flux that Kubera is in today. In this release, KONVOY E2E became a stable pipeline alongside AWS E2E. This is a significant improvement since KONVOY pipeline is an on premise cluster setup on VMware VMs. It takes into account VM snapshots to bring up the K8s clusters fast. A big shoutout to @Aman Gupta and @giri to make this happen.

### Rancher E2E Pipeline
In addition to AWS and KONVOY, E2E uses Rancher as a Kubernetes platform to run end to end test cases. Rancher pipeline still continues to face a lot of issues. This has led to either its pipeline runs getting cancelled or marked as failed. It was due to frequent reboots of underlying VMware VMs. As of today, these VMs have their motherboard replaced and things have started to look fine. Team will work to elevate Rancher as a stable pipeline in upcoming release.

### GitLab license renewal
Team had a bad experience with GitLab when it had become the single point of failure. The root cause for this SPOF was GitLab's certificate getting expired. Hence, team was on alert when GitLab started sending notifications on its license renewal. Team spent no time in renewing the license and hence eliminated a possible disaster.

### What's next?
Following are the two new projects that E2E team is pursuing:
- https://github.com/mayadata-io/kubera-api-testing
- https://github.com/kubera-io/continuous-kubernetes

**kubera-api-testing** is a development effort undertaken to simplify testing Kubera APIs. Team currently uses Ansible, kubectl & bunch of bash scripts to test the APIs. Needless to say it is fragile and does not help in identifying root cause of error(s) if any. kubera-api-testing aims to eliminate these problems. In addition to testing Kubera APIs it can test Kubernetes APIs in case such a need arise.

**continuous-kubernetes** aims to provide E2E badges by automating various end user use cases. One can use this repo to find working recipe(s) to validate their user story. In other words one can verify if following combination for example works or not:
- Cassandra (KUDO) + OpenEBS local pv (host path) + GKE
- Cassandra (KUDO) + OpenEBS local pv (host path) + EKS
- Cassandra (DataStax) + OpenEBS local pv (device) + Konvoy

Above is a sample of possible combinations. There can be hundreds of them in reality. Team aims to implement these user stories using following approaches:
- provide declarative recipes
- make them gitops friendly
- avoid the need to write hundreds of lines of code

### Roadmap
E to E team need to tackle lot of unknowns like:
- Pipeline does not help in identifying the root cause of errors
- Inability to run the testcases outside of the pipeline infrastructure
- Pipelines take longer times to execute (3 to 5 hours)
- Infrastructure setup is not declarative making it hard to maintain

#### E to E team will continue to focus on the following
- Develop or use declarative tools to:
    - setup & dispose Kubernetes clusters
    - exercise granular control to run tests, stages & pipelines
    - write integration as well as e2e test cases
    - find the root cause of errors in the pipelines
    - to analyse current state of release from E2E metrics
- Implement e2e test cases from users' view of the world
  - i.e. validate & verify managing workloads on Kubera
    - Run Day 0, Day 1, and Day 2 operations
    - Run performance benchmarks
    - Provide best practices guidelines w.r.t workloads
  - In short, think & act like a Kubernetes SRE
- Be Kubernetes advocates for CI CD as well as workloads

### Appendix
- SPOF - Single Point of Failure
- E to E - End to End