---
id: provisioning
title: OpenEBS Install, Upgrade & Provisioning
sidebar_label: Test Strategy
---
------

## OpenEBS
This page captures the test scenarios for OpenEBS operations
- Install
- Upgrade
- Volume Provisioning 


###  OpenEBS Install

- [ ] TCID-DIR-OP-BD-VIEW-ALL - View devices of a kubernetes cluster
- [ ] TCID-DIR-OP-BD-VIEW-SCALE - View devices on a scaled kubernetes cluster
- [ ] TCID-DIR-OP-BD-VIEW-SCALE-RESTART - View devices on a scaled kubernetes cluster even after multiple restarts of this cluster is observed
- [ ] TCID-DIR-OP-BD-FILTER-SSD - View SSD based devices of a kubernetes cluster
- [ ] TCID-DIR-OP-BD-FILTER-PATH - View devices with specific path across the kubernetes cluster
- [ ] TCID-DIR-OP-BD-IGNORE - Avoid devices from specific nodes of a kubernetes cluster
- [ ] TCID-DIR-OP-BD-VIEW-TOGGLE - Toggle viewing devices from specific nodes of a kubernetes cluster



| TCID                                                                   | Konvoy | AWS  |
| ---------------------------------------------------------------------- | ------ | ---- |
| [TCID-DIR-OP-BD-VIEW-ALL](TCID-OP-DIR-BD-VIEW-ALL)                     | N      | N    |
| [TCID-DIR-OP-BD-VIEW-SCALE](TCID-OP-DIR-BD-VIEW-SCALE)                 | N      | N    |
| [TCID-DIR-OP-BD-VIEW-SCALE-RESTART](TCID-DIR-OP-BD-VIEW-SCALE-RESTART) | N      | N    |
| [TCID-DIR-OP-BD-FILTER-SSD](TCID-OP-DIR-BD-FILTER-SSD)                 | N      | N    |
| [TCID-DIR-OP-BD-FILTER-PATH](TCID-DIR-OP-BD-FILTER-PATH)               | N      | N    |
| [TCID-DIR-OP-BD-IGNORE](TCID-DIR-OP-BD-IGNORE)                         | N      | N    |
| [TCID-DIR-OP-BD-VIEW-TOGGLE](TCID-DIR-OP-BD-VIEW-TOGGLE)               | N      | N    |


#### Test Results
- TODO - Provide the links


###  OpenEBS Control Plane Upgrade


| TCID | Brief Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |
|      |                   |        |
|      |                   |        |

### OpenEBS Data Plane Upgrade


| TCID | Brief Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |
|      |                   |        |
|      |                   |        |


### CStor Pool Recommendations 
- [ ] TCID-DIR-OP-CSP-REC-LIST - List all cstor pool recommendations
- [ ] TCID-DIR-OP-CSP-REC-LIST-NO-NDM - List all cstor pool recommendations with NDM not running
- [ ] TCID-DIR-OP-CSP-REC-LIST-STRIPE - List all stripe cstor pool recommendations
- [ ] TCID-DIR-OP-CSP-REC-LIST-MIRROR - List all mirror cstor pool recommendations
- [ ] TCID-DIR-OP-CSP-REC-CREATE-MIRROR - Create mirror cstor pool cluster
- [ ] TCID-DIR-OP-CSP-REC-CREATE-STRIPE - Create stripe cstor pool cluster

| TCID                                                                    | Konvoy | AWS  |
| ----------------------------------------------------------------------- | ------ | ---- |
| [TCID-DIR-OP-CSP-REC-LIST](TCID-DIR-OP-CSP-REC-LIST)                    | N      | N    |
| [TCID-DIR-OP-CSP-REC-LIST-NO-NDM](TCID-DIR-OP-CSP-REC-LIST-NO-NDM)      | N      | N    |
| [TCID-DIR-OP-CSP-REC-LIST-STRIPE](TCID-DIR-OP-CSP-REC-LIST-STRIPE)      | N      | N    |
| [TCID-DIR-OP-CSP-REC-LIST-MIRROR](TCID-DIR-OP-CSP-REC-LIST-MIRROR)      | N      | N    |
| [TCID-DIR-OP-CSP-REC-CREATE-MIRROR](TCID-DIR-OP-CSP-REC-CREATE-MIRROR)  | N      | N    |
| [TCID-DIR-OP-CSP-REC-CREATE-STRIPE](TCID-DIR-OP-CSP-REC-CREATE-STRIPE)  | N      | N    |


- #### Jiva Pool Provisioning 

- [ ] TCID-DIR-OP-JIVA-OK-RESTART - Jiva volumes should run even after multiple restarts of my kubernetes cluster is observed

| TCID | Brief Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |

- #### LocalPV Pool Provisioning 


| TCID | Brief Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |

##  Storage Class Provisioning

- cStor
- Jiva
- Local PV Hostpath
- Local PV Device

| TCID | Brief Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |
|      |                   |        |
|      |                   |        |



##  Volume  Provisioning

- cStor
- Jiva
- Local PV Hostpath
- Local PV Device

| TCID | Brief Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |
|      |                   |        |
|      |                   |        |

## Glossary

| Abbreviation     | Details                           |
| ---------------- | --------------------------------- |
| TCID             | TestCase ID                       |
| DIR              | Director                          |
| DAO              | Data Agility Operator             |
| CPA              | CstorPool Auto                    |
| OP               | OpenEBS Provisioning              |
| OO               | OpenEBS Operator                  |
| LBL              | Labels                            |
| ANN              | Annotations                       |
| SPEC             | Specifications                    |
| RST              | Restart                           |
| NDM              | Node Device Manager               |
| REC              | Recommendations                   |
| BD               | BlockDevice                       |
| BDC              | BlockDeviceClaim                  |
| PSP              | PodSecurityPolicy                 |
