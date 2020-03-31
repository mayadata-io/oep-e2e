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
- Install Director with all three databases as OpenEBS cStor with locall SSDs underneath.

### Actual test cases

| TestCase                               | Breif Description                 | #Issue       | Platform | Status  |
| -------------------------------------- | --------------------------------- | ------------ | -------- | ------- |
| [Dir-Install-GCP](install-tcid-iudi01) | Install DOP using helm on GCP     | Not-assigned | GCP      | In-Prod |
| [Dir-Install-GCP](install-tcid-iudi02) | Install DOP using openebs local pv| Not-assigned | GCP      | Not-done|
| [Dir-Install-GCP](install-tcid-iudi03) | Install DOP using openebs local pv| Not-assigned | GCP      | Not-done|
|                                        |                                   |              |          |         |
|                                        |                                   |              |          |         |

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

