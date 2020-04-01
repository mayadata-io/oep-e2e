---
id: directorInstall
title: Install and Upgrade of Director
sidebar_label: Test Strategy
---
------

This page captures the test scenarios for installation of Director OnPrem, upgrading Director OnPrem. 

## Installation of Director OnPrem

Testing does not cover the usability aspects of Director OnPrem. It covers the installation scenarios under various combinations storage classes, different platforms, different network plugins and different resource constraints.



### Installation test strategy or scenarios

Director has three databases : mysql for user data, Cassandra for monitoring and alert metrics and ElasticsearchDB for logs. Director needs to be tested with various combinations of storage and resources for these databases

- Install Director with all three databases as LocalPV with GPD/EBS underneath.
- Install Director with all three databases as OpenEBS LocalPV with local SSDs underneath.
- Install Director with all three databases as OpenEBS LocalPV with GPD/EBS underneath.
- Install Director with all three databases as OpenEBS cStor with local SSDs underneath.
- Install Director using only openebs-jiva-default storage class.
- Install Director using cstor,jiva and local-pv storage class.

### Dop installation

| TCID                                   | TC Name                   | GCP             | Rancher | Konvoy | AWS  |
| -------------------------------------- | ------------------------- | --------------- | ------- | ------ | ---- |
| [tcid-iudi01](tc-install-gcp-std)      | TC-Install-GCP-STD        | Y               | W       | W      | W    |
| [tcid-iudi02](tc-install-gcp-ssdlpv)   | TC-Install-GCP-SSDLPV     | W               | W       | W      | W    |
| [tcid-iudi03](tc-install-gcp-gpdlpv)   | TC-Install-GCP-GPDLPV     | W               | W       | W      | W    |
| [tcid-iudi04](tc-install-gcp-cstor)    | TC-Install-GCP-Cstor	     | W               | W       | W      | W    |
| [tcid-iudi05](tc-install-gcp-jiva)     | TC-Install-GCP-Jiva	     | W               | W       | W      | W    |
| [tcid-iudi06](tc-install-gcp-allsc)    | TC-Install-GCP-Allsc	     | W               | W       | W      | W    |




## Upgrade of Director OnPrem

Upgrade of Director consists of upgrading the Director micro services and upgrading underlying databases when needed.

### Upgrade scenarios

- Upgrade using helm chart
- Upgrade the underlying databases manually using database operators or otherwise

### Actual test cases

| TCID | Breif Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |
|      |                   |        |
|      |                   |        |

