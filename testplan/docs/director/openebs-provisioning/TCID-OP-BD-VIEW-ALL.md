---
id: TCID-OP-BD-VIEW-ALL
title: View devices across the kubernetes cluster
sidebar_label: TCID-OP-BD-VIEW-ALL
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
    <td> TCID-OP-BD-VIEW-ALL </td>
    <td> BlockDevice </td>
    <td> View all available devices across the kubernetes cluster </td>
  </tr>
</table>

### Setup
- Kubernetes _(K8s)_ cluster should be running

### Steps
- Install DirectorOnPrem _(DOP)_ on this K8s cluster
- Install OpenEBS using DOP

### Expectations
- Users should be able to list devices attached to this K8s cluster
- Users should be able to categorize device types e.g. HDD, SSD, etc

### Notes to the Reviewer
- This is a postive test case
- Recent versions of K8s & DOP needs to be used

### Test Results
Access test results across various platforms by navigating through following links
- [Link]()