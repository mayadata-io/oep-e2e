---
id: TCID-OP-BD-VIEW-TOGGLE
title: View or ignore specific devices in a kubernetes cluster
sidebar_label: TCID-OP-BD-VIEW-TOGGLE
---
------

### Experiment Metadata

<table>
  <tr>
    <th> TCID </th>
    <th> Type </th>
    <th> Description </th>
  </tr>
  <tr>
    <td> TCID-OP-BD-VIEW-TOGGLE </td>
    <td> BlockDevice </td>
    <td> View or ignore specific devices in a kubernetes cluster </td>
  </tr>
</table>

### Setup
- Kubernetes _(K8s)_ cluster should be running

### Steps
- Install DirectorOnPrem _(DOP)_ on this K8s cluster
- Install OpenEBS using DOP
- OpenEBS should be installed on nodes meant for storage
- OpenEBS should be updated to make use of new nodes for storage

### Expectations
- Users should not be able to view devices that are not meant to be consumed for storage
- Users should be able to view devices from nodes that are included as part of OpenEBS

### Notes to the Reviewer
- This is a positive test case
- Recent versions of K8s & DOP needs to be used

### Test Results
Access test results across various platforms by navigating through following links
- [Link]()