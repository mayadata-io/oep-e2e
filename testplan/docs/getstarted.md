---
id: getstarted
title: Test Plan for MayaData OpenEBS Enterprise Platform (OEP)
sidebar_label: Introduction
---
------

MayaData delivers it's vision of delivering data agility for DevOps by transforming Kubernetes into a data layer. MayaData's product is called OpenEBS Enterprise Platform or OEP. OEP is a combination of multiple tools and projects and it currently comprises of OpenEBS Enterprise Edition, Director and Litmus. OEP being an enterprise grade product, requires highest levels of testing such as scalability, security, interoperability, functional and chaos engineering. This site covers all these areas and serves as the top level guide for those who are contributing to the quality of the product.



## Test Plan Artifacts:

**Master Test Plan Site** - This site

**Master Test Plan YAML** - [A coded version of this site](https://github.com/mayadata-io/oep-e2e/blob/master/.master-plan.yml), that has unique test cases IDs corresponding to each test case. This helps in determining the overall coverage.

**Test Case** - Each test case will have two parts:
- Detailed description of the test case _(somewhere in this site)_, &
- Actual implementation of the test case _(code)_

**GitHub issues** - [Issues or backlogs](https://github.com/mayadata-io/oep-e2e/issues) are the entry points to the quality feedback process. These issues track the test plan completion including and implemention of actual test cases.


## Test repository structure:

**oep-e2e** is the main repository that hosts the test plans and test cases. This is also the repository that hosts the source code of this site. 

**oep-e2e-gcp** repository contains scripts to run test cases against GCP platform.

**oep-e2e-rancher** repository contains scripts to run test cases against Rancher platform.

**oep-e2e-konvoy** repository contains scripts to run test cases against D2IQ Konvoy platform.



## Contributing guidelines:

- You can [create a GitHub issue](https://github.com/mayadata-io/oep-e2e/issues/new/choose) if you are having an idea for improvement or to notify a missing test area/case.
- If you want to suggest changes to any page in the test plan, use 'Edit this page' link found towards the bottom left corner of the specific page. This will enable you to raise a pull request with your suggested changes.







