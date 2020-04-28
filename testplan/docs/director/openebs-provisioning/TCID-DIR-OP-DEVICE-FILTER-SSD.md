---
id: TCID-DIR-OP-DEVICE-FILTER-SSD
title: Filter devices in a kubernetes cluster
sidebar_label: TCID-DIR-OP-DEVICE-FILTER-SSD
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
    <td> TCID-DIR-OP-DEVICE-FILTER-SSD </td>
    <td> BlockDevice </td>
    <td> Filter devices in a kubernetes cluster </td>
  </tr>
</table>

### Setup
- Kubernetes _(K8s)_ cluster should be running

### Steps
- Install DirectorOnPrem _(DOP)_ on this K8s cluster
- Install OpenEBS using DOP

### Expectations
- Users should be able to list devices attached to this K8s cluster
- Users should be able to filter SSD based devices

### Notes to the Reviewer
- This is a positive test case
- Recent versions of K8s & DOP needs to be used

### Test Results
Access test results across various platforms by navigating through following links
- [Link]()