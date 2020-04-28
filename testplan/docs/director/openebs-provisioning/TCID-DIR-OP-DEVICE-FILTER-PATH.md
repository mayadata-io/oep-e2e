---
id: TCID-DIR-OP-DEVICE-FILTER-PATH
title: View devices at specific paths in a kubernetes cluster
sidebar_label: TCID-DIR-OP-DEVICE-FILTER-PATH
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
    <td> TCID-DIR-OP-DEVICE-FILTER-PATH </td>
    <td> BlockDevice </td>
    <td> View devices at specific path in a kubernetes cluster </td>
  </tr>
</table>

### Setup
- Kubernetes _(K8s)_ cluster should be running

### Steps
- Install DirectorOnPrem _(DOP)_ on this K8s cluster
- Install OpenEBS using DOP
- Install OpenEBS on nodes meant for storage
- Set OpenEBS to discover devices at specific paths

### Expectations
- Users should be able to view devices at specific paths

### Notes to the Reviewer
- This is a positive test case
- Recent versions of K8s & DOP needs to be used

### Test Results
Access test results across various platforms by navigating through following links
- [Link]()