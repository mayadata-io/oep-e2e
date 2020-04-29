---
id: installation
title: Director Install and Upgrade
sidebar_label: Test Strategy
---
------

This page captures the test scenarios for following:
1/ installation of DirectorOnPrem _(DOP)_ &
2/ upgrade of DOP

Director uses three different databases namely:
- `MySQL` for user data,
- `Cassandra` for monitoring and alerts, &
- `ElasticsearchDB` for logs

As a DevOps admin, I want to test compatibility of Director in consuming storage from different openebs engines. This helps me in planning my infrastructure for my cluster. I want to know the install & upgrade behaviour of Director based on following combinations:

- Director with all its databases consuming openebs device based local pv. The devices in turn would be using GPD/EBS disks.
- Director with all its databases consuming openebs device based local pv. The devices would be using local SSDs underneath.
- Director with all its databases consuming openebs cstor engine with local SSDs underneath.


### TCID-DIR-INSTALL-ON

| TCID                                                         | RANCHER | AWS | KONVOY|
|------------------------------------------------------------- |-------- |-----|-------|
|[TCID-DIR-INSTALL-ON-LOCAL-DEV](TCID-DIR-INSTALL-ON-LOCAL-DEV)|         |     |       |
|[TCID-DIR-INSTALL-ON-LOCAL-HP](TCID-DIR-INSTALL-ON-LOCAL-HP)  |         |     |       |
|[TCID-DIR-INSTALL-ON-CSTOR](TCID-DIR-INSTALL-ON-CSTOR)        |         |     |       |


### TCID-DIR-UPGRADE-ON

| TCID                                                         | RANCHER | AWS | KONVOY|
|------------------------------------------------------------- |-------- |-----|-------|
|[TCID-DIR-UPGRADE-ON-LOCAL-DEV](TCID-DIR-UPGRADE-ON-LOCAL-DEV)|         |     |       |
|[TCID-DIR-UPGRADE-ON-LOCAL-HP](TCID-DIR-UPGRADE-ON-LOCAL-HP)  |         |     |       |
|[TCID-DIR-UPGRADE-ON-CSTOR](TCID-DIR-UPGRADE-ON-CSTOR)        |         |     |       |