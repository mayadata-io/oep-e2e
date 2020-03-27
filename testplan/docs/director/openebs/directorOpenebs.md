---
id: directorOpenebs
title: OpenEBS Installation, Upgrade and Provisioning
sidebar_label: Summary
---
------

This page captures the test scenarios for the following management of OpenEBS component from DOP
- Installation
- Upgrade
- Provisioing 


###  OpenEBS Installation
OpenEBS install can be performed by director, the following options are supported
- Basic
  In basic installation, its almost similar to operator.yaml installation directly from the openebs docs. Later User can go ahead and select the nodes on which data plane components can be done
- Advanced
 In this installation mode, user can customize which node control plane and dataplane components can be installed. Also would be able to do the customize - NDM :- Path filters, Vendor, OS Disks
 - Resource limits :- CPU, RAM


###  OpenEBS Upgrade
OpenEBS upgrade can be performed in the following order

  1.  Control plane upgrade

This is supported only for OpenEBS installation done via DOP. 

| TCID | Breif Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |
|      |                   |        |
|      |                   |        |

  2.  Data plane upgrade

This can be perfromed only post Control plane components are upgraded. Data plane upgrade is supported for any mode of OpenEBS installation i.e OpenEBS dataplane can be upgraded for non DOP installed case as well.

| TCID | Breif Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |
|      |                   |        |
|      |                   |        |

###  Pool Provisioning
- #### cStor Pool Provisioning 


| TCID | Breif Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |
|      |                   |        |
|      |                   |        |

- #### Jiva Pool Provisioning 


| TCID | Breif Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |

- #### LocalPV Pool Provisioning 


| TCID | Breif Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |

##  Storage Class Provisioning

- cStor
- Jiva
- Local PV Hostpath
- Local PV Device

| TCID | Breif Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |
|      |                   |        |
|      |                   |        |



##  Volume  Provisioning

- cStor
- Jiva
- Local PV Hostpath
- Local PV Device

| TCID | Breif Description | #Issue |
| ---- | ----------------- | ------ |
|      |                   |        |
|      |                   |        |
|      |                   |        |

