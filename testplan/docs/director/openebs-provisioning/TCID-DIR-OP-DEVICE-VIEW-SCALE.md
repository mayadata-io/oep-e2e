---
id: TCID-DIR-OP-DEVICE-VIEW-SCALE
title: View devices in a scaled kubernetes cluster
sidebar_label: TCID-DIR-OP-DEVICE-VIEW-SCALE
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
    <td> TCID-DIR-OP-DEVICE-VIEW-SCALE </td>
    <td> BlockDevice </td>
    <td> View devices across a scaled kubernetes cluster </td>
  </tr>
</table>

### Setup
- Kubernetes _(K8s)_ cluster should be running

### Steps
- Install DirectorOnPrem _(DOP)_ on this K8s cluster
- Install OpenEBS using DOP
- K8s cluster should have large number of nodes
  - Availability of three or more nodes in the cluster is recommended
- K8s nodes should have large number of disks attached to the former
  - Availability of **20** or more disks per node is recommended

### Expectations
- Users should be able to list devices attached to this K8s cluster
- Users should be able to categorize device types e.g. HDD, SSD, etc
- Users should be able to identify devices categorized by nodes

### Notes to the Reviewer
- This is a postive test case
- Recent versions of K8s & DOP needs to be used

### Test Results
Access test results across various platforms by navigating through following links
- [Link]()