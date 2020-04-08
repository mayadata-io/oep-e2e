---
id: dao 
title: Data Agility Operators
sidebar_label: Test Strategy
---
------

## DAOs

Data Agility Operators consist of one or more Kubernetes operators that automate OpenEBS operations. They are built upon Kubernetes custom resources making them gitops friendly as well as easy to be invoked via third party tools. Following are current set of DAOs:

- [OpenEBS Operator](https://github.com/mayadata-io/openebs-upgrade)
- [CStorPool Auto](https://github.com/mayadata-io/cstorpoolauto)
- [Storage Provisioner](https://github.com/mayadata-io/storage-provisioner)

## OpenEBS Operator

- [ ] TC-DAO-OO-BD-LBL-RST  - BlockDevice labels should persist across NDM restarts
- [ ] TC-DAO-OO-BD-ANN-RST  - BlockDevice annotations should persist across NDM restarts
- [ ] TC-DAO-OO-BD-SPEC-RST - BlockDevice spec should persist across NDM restarts

| TCID                                               | Konvoy | GKE  |
| -------------------------------------------------- | ------ | ---- |
| [tcid-dao-oo-bd-lbl](TC-DAO-OO-BD-LBL)             | N      | N    |


### Glossary

| Abbreviation     | Details                           |
| ---------------- | --------------------------------- |
| TC               | TestCase                          |
| DAO              | Data Agility Operator             |
| CPA              | CstorPool Auto                    |
| OO               | OpenEBS Operator                  |
| LBL              | Labels                            |
| ANN              | Annotations                       |
| SPEC             | Specifications                    |
| RST              | Restart                           |
