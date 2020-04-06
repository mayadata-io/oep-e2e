---
id: TCID-OP-BD-IGNORE
title: Ignore specific devices in a kubernetes cluster
sidebar_label: TCID-OP-BD-IGNORE
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
    <td> TCID-OP-BD-IGNORE </td>
    <td> BlockDevice </td>
    <td> Ignore specific devices in a kubernetes cluster </td>
  </tr>
</table>

### Setup
- Kubernetes _(K8s)_ cluster should be running

### Steps
- Install DirectorOnPrem _(DOP)_ on this K8s cluster
- Install OpenEBS using DOP
- Install OpenEBS on nodes meant for storage

### Expectations
- Users should not be able to view devices that are not meant to be consumed for storage

### Notes to the Reviewer
- This is a positive test case
- Recent versions of K8s & DOP needs to be used

### Test Results
Access test results across various platforms by navigating through following links
- [Link]()