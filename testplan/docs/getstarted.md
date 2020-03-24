---
id: getstarted
title: Test Plan for OpenEBS Enterprise Edition
sidebar_label: Introduction
---
------

## Test Plan for OpenEBS Enterprise Edition or OEP

OEP, as the enterprise edition of the product, requires highest level of testing interms of covering areas of testing such as scalability, security, interoperability, functional and chaos engineering. This test plan covers all these areas and serves as the top level guide for those who are contributing to the quality of the product.



## Test artifacts:

**Master Test Plan** - This is the master plan for planning the testing.

**Master-test-yaml** - [A coded version of this plan](https://github.com/mayadata-io/oep-e2e/blob/master/.master-plan.yml), which will allocate unique test IDs for each test case so that they are checked against the test runs in pipelines to calculate the coverage.

**Test case** - Each test case will have two parts.

- Detailed description of the test case and
- Actual implementation of the test case

**GitLab issues** - [Issues or backlogs](https://github.com/mayadata-io/oep-e2e/issues) are the entry points to the quality feedback process. These issues also serve as the tracking aids for maintaining the test plan and implementing the test cases.



## Test repository structure:

`oep-e2e` is the main repository that hosts the test plan and test cases and some elements of test cases implementations such as litmus wrappers. 

`oep-e2e-gcp` is the repository containing implementation of test cases specific to GCP platform.

`oep-e2e-rancher` is the repository containing implementation of test cases specific to Rancher platform.

`oep-e2e-konvoy` is the repository containing implementation of test cases specific to D2IQ Konvoy platform.



## Contributing guidelines:

- You can [create a GitHub issue](https://github.com/mayadata-io/oep-e2e/issues/new/choose) if you are having an idea for improvement or to notify a missing test area/case.
- If you want to suggest new changes to this page or any other page in the test plan, use the `Edit` button on the top right corner of the specific page. 







