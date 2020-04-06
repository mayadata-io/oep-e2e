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

### Supported method will be 

- standard sc
- OpenEBS localPV (Recommended)
- OpenEBS cStor
- OpenEBS Jiva (Not Recommended)

### List of uncovered scenarios 

- DOP installation using 3 different storage class such as cstor-storage-class,openebs-jiva-default and openebs-hostpath.
- Install Director using only openebs-jiva-default storage class.

### Dop installation

| TCID                                   | TC Name                   | GCP             | Rancher | Konvoy | AWS  |
| -------------------------------------- | ------------------------- | --------------- | ------- | ------ | ---- |
| [tcid-iudi01](tc-install-gpd-std)      | TC-Install-GPD-Std        | Y               | W       | W      | W    |
| [tcid-iudi02](tc-install-ssd-lpv)      | TC-Install-SSD-Lpv        | W               | Y       | Y      | W    |
| [tcid-iudi03](tc-install-gpd-lpv)      | TC-Install-GPD-Lpv        | W               | W       | W      | W    |
| [tcid-iudi04](tc-install-ssd-cstor)    | TC-Install-SSD-Cstor	     | W               | W       | W      | W    |




## Upgrade of Director OnPrem

Upgrade of Director consists of upgrading the Director micro services and upgrading underlying databases when needed.

### Upgrade scenarios

- Upgrade using helm chart when sc is standard.
- Upgrade using helm chart when sc is localPV.
- Upgrade using helm chart when sc is cstor.
- Upgrade the underlying databases manually using database operators or otherwise.


### Dop upgrade

| TCID                                   | TC Name                   | GCP             | Rancher | Konvoy | AWS  |
| -------------------------------------- | ------------------------- | --------------- | ------- | ------ | ---- |
| [tcid-iudu01](tc-upgrade-gpd-std)      | TC-Upgrade-GPD-Std        | W               | W       | W      | W    |
| [tcid-iudu02](tc-upgrade-ssd-lpv)      | TC-Upgrade-SSD-Lpv        | W               | W       | W      | W    |
| [tcid-iudu03](tc-upgrade-ssd-cstor)    | TC-Upgrade-SSD-Cstor      | W               | W       | W      | W    |
