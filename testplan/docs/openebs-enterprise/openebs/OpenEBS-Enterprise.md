---
id: OpenEBS-Enterprise 
title: OpenEBS Enterprise
sidebar_label: Test Strategy
---
------

## OpenEBS EE (OpenEBS Enterprise)

OpenEBS EE is Enterprise version of OpenEBS certified by MayaData. This goes through rigorous testing in-addition to the testing covered as part of community edition <a href="http://openebs.ci/" target="_blank">openebs.ci</a> 

Testcases cover for the following 

- Install and Upgrade - Install and upgrade of OpenEBS can be done in following ways
  - Helm
  - Director - Testing of Install and Upgrade is covered in [Director](/docs/director/openebs-provisioning/plan) 
- Provisioning - Provisioning of Storage Engines can be done in following ways
  - Yaml Spec
  - Director - Testing of provisioning via Director is covered in [Director](/docs/director/openebs-provisioning/plan) 
- Storage Engines - OpenEBS Supports multiple storage engine as listed below
  - cStor
  - Local PV Hostpath
  - Local PV Device
  - Jiva
  - ZFS on Local PV
  - MayaStor

- Soak Testing

- Security Testing

- Performance

- Reliability 

- Scalability 

  