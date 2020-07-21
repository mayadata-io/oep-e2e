---
id: kubera-e2e-release-1-11
title: Kubera E2E Release 1.11
sidebar_label: Kubera E2E 1.11
---

## RELEASE NOTES
This is the second release of Kubera end to end (E2E) pipelines. This release proved to be a painful one considering the number of blockers that had to be taken care of. This note will focus on these blockers and their resolutions. One will also notice a change in our strategy from being coverage focused to getting the pipeline infrastructure stable. We also have started spending time on manual testing followed by automated & back to manual testing based cycles within a single sprint to unearth as many bugs as possible.

### OnPrem Rancher Pipeline
Rancher is one of the Kubernetes platforms that E to E uses to run its test cases. Rancher is set up as a on-prem cluster on ESX Virtual Machines. A Rancher Kubernetes cluster runs as a single master node with multiple worker nodes. Some of the Rancher clusters is composed of 3 worker nodes while others are made up of 5 worker nodes. E to E calls them as Cluster 1, 2 & 3.

A single E to E pipeline is made to run on these clusters by a Gitlab cluster running on AWS. This pipeline consists of multiple Gitlab stages with each stage consisting of multiple jobs. Each job is considered as a test case by E to E team. These jobs are in-turn used to provide the E to E coverage.

It was observed that Rancher based pipeline failed on almost every run. However, the root casue of failure was different on each run. In other words, each pipeline run would result in failure of one or more jobs which would change for the next run. We were not sure if these jobs i.e. test cases were flaky or the entire Rancher cluster was flaky. Since we could not find any genuine issues with these jobs, we started looking more closely into the cluster itself. Some of these cluster VMs are restored from a particular state on every pipeline run. The VM snapshots and restores were done via ESX. We had included the memory state of the VM while taking the machine's snapshot. This results in old processes appearing in the newly restored state. This in turn resulted in pipeline failures since pipeline expects exact state before running the tests. Once we started excluding memory from snapshots, the pipeline started to work fine.

### OnPrem Konvoy Pipeline
Konvoy too is an on-prem pipeline that runs in exactly the same way as described above for Rancher.

It was observed that none of the Director pods got deployed while installing Kubera Director. The issue was very persistent and was reproducible when running the test case via manual approaches. Finally, the root cause pointed to lack of space in VM that in turn resulted in slow downloads of container images and hence failure to run the pipelines successfully.

### Gitlab cluster became the SPOF
All the E to E on-prem clusters were managed from a single Gitlab cluster running in an AWS cloud instance. This Gitlab instance had its certificate expired which in turn resulted in blocking all the pipelines from running. Things started to work fine when the certificate was renewed.

### Lab to Registry connectivity
All the on-prem Kubernetes clusters sources Kubera Director container images from registry.mayadata.io. It was observed that Kubernetes clusters were not able to download images from this private registry. On further investigation it was found that the images from this particular registry took lot of time  _(more than 5 minutes)_ and hence resulted in timeouts. However, the same registry was able to serve the images pretty fast _(in less than a minute)_ to other clusters that were not in our lab network. This seems to be a case of throttling between specific client & server connection. We shall attempt to mirror 'registry.mayadata.io' with a new registry inside our lab itself. We beleive this indirection should help unblock the pipelines from getting into the throttling connectivity issue. In addition, we might also come up with a script that will pre pull all images _(even if it takes a lot of time)_ to all the cluster nodes before carrying out the tests.

### Change of Strategy
Based on our recent E to E experiences we have decided to change our test strategy. Team will focus on manual testing, doc updates, project planning, pipeline changes in the first week of release sprint. Subsequent two weeks will be spent on developing automated test cases. Final week i.e. week of release will be spent on manual testing only. This change has been done with the sole purpose of catching bugs early in the lifecycle. This should also take care of limiting the impact of flaky tests or pipelines or both to a limited span during the entire sprint. It is to be noted that pipelines will be run daily irrespective of the test strategy that team will be following.

_Team will not add new GUI / Selenium test cases & instead focus more on API testing. This will be done till GUI screens are stable._

### Roadmap
E to E team need to tackle lot of unknowns some of which are listed below:
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
    - Run Day 0, Day 2 operations
    - Run performance benchmarks
    - Provide best practices guidelines w.r.t workloads
  - In short, think & act like a Kubernetes SRE
- Be Kubernetes advocates for CI CD as well as workloads

### Appendix
- SPOF - Single Point of Failure
- E to E - End to End
- GUI - Graphical User Interface