---
id: kubera-e2e-release-1-10
title: Kubera E2E Release 1.10
sidebar_label: Kubera E2E 1.10
---

## RELEASE NOTES
This is the very first release of Kubera and also the first release of Kubera end to end (E2E) pipelines. In this release, E2E team was busy setting up of on-premise as well as cloud lab infrastructures, setting up Kubernetes platforms _(e.g. Rancher, AWS, Konvoy)_, adding component specific test cases, & setting up of selenium environment to test Director. In addition, E2E team implemented a basic [dashboard](https://oep-pipelines.mayadata.io/) to present a high level overview of various pipelines against the Kubernetes platforms these pipelines were run against.

### Coverage as a measuring unit
This release focussed on making coverage as one of the indicators to determine the state of testing _(read progress, efficiency, etc)_. Coverage calculation is very simple. We make use of `implemented test case count` as numerator against `desired test case count` as the denominator to derive the coverage. Multiplying this fraction with `100` provides the coverage value in percentage.

A minimum test coverage of **35%** was agreed upon to grant a go ahead for this release.

### What does the future look like?
While there is no doubt on the progress this team made; there were a lot of unknowns that needs to be understood & taken care of. There were several unknowns experienced in this release. Some of them are listed below:
- Rancher platform experienced a lot of kube api server timeout errors
- Pipeline logs were not able to determine the root cause of errors
- Inability to run the testcases outside of the pipeline infrastructure
- Pipelines took longer times to execute
- Infrastructure setup was not declarative making it hard to update & restore

E2E team will have following responsibilities going forward:
- Build tooling to manage disposable Kubernetes platforms
- Build tooling that provides granular control to execute test cases, stages & pipelines
- Build tooling that help teams to write integration as well as e2e test cases without steep learning curves
- Build tooling that help teams to find the root cause of errors in the pipelines
- Build tooling that help one in analysing the current state of release from E2E metrics
- Implement e2e test cases from users' view of the world
  - In other words validate & verify managing workloads on Kubera
  - Includes Day 0, Day 2 operations
  - Includes providing performance benchmarks
  - Includes providing best practices guidelines w.r.t workloads
  - In short, think & act like a Kubernetes SRE
- Be Kubernetes advocates for CI CD as well as workloads