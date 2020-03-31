---
id: directorOpenEBS
title: OpenEBS Installation, Upgrade and Provisioning
sidebar_label: Test Strategy
---
------

## OpenEBS
This page captures the test scenarios for various OpenEBS features
- Installation
- Upgrade
- Provisioing 


###  OpenEBS Installation
OpenEBS install performed by director has following options:
- Basic
  In basic installation, its almost similar to operator.yaml installation directly from the openebs docs. Later User can go ahead and select the nodes on which data plane components can be done
- Advanced
 In this installation mode, user can customize the node on which control plane and dataplane components are installed. There are other tunables like for example NDM based path filters, vendor & OS disk selection.


###  OpenEBS Upgrade
OpenEBS upgrade can be performed in the following order

  1.  Control plane upgrade

This is supported only for OpenEBS installation done via DOP. 

| TCID | Brief Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |
|      |                   |        |
|      |                   |        |

  2.  Data plane upgrade

This can be perfromed only post Control plane components are upgraded. Data plane upgrade is supported for any mode of OpenEBS installation i.e OpenEBS dataplane can be upgraded for non DOP installed case as well.

| TCID | Brief Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |
|      |                   |        |
|      |                   |        |

###  Pool Provisioning
- #### cStor Pool Recommendations 
  - [ ] tc-csp-rec-list - List all cstor pool recommendations
  - [ ] tc-csp-rec-list-no-ndm - List all cstor pool recommendations with NDM not running
  - [ ] tc-csp-rec-list-stripe - List all stripe cstor pool recommendations
  - [ ] tc-csp-rec-list-mirror - List all mirror cstor pool recommendations
  - [ ] tc-csp-rec-create-mirror - Create mirror cstor pool cluster
  - [ ] tc-csp-rec-create-stripe - Create stripe cstor pool cluster

| TCID                                        | TC NAME                 | Konvoy | GKE  |
| ------------------------------------------- | ----------------------- | ------ | ---- |
| [tcid-csprec001](tc-csp-rec-list)           | tc-csp-rec-list         | N      | N    |
| [tcid-csprec002](tc-csp-rec-list-no-ndm)    | tc-csp-rec-list-no-ndm  | N      | N    |
| [tcid-csprec003](tc-csp-rec-list-stripe)    | tc-csp-rec-list-stripe  | N      | N    |
| [tcid-csprec004](tc-csp-rec-list-mirror)    | tc-csp-rec-list-mirror  | N      | N    |
| [tcid-csprec005](tc-csp-rec-create-mirror)  | tc-csp-rec-create-mirror| N      | N    |
| [tcid-csprec006](tc-csp-rec-create-stripe)  | tc-csp-rec-create-stripe| N      | N    |


- #### Jiva Pool Provisioning 


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

