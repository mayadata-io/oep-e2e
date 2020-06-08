---
id: TCID-DIR-OP-DEVICE-VIEW-SCALE-RESTART
title: View devices in a scaled kubernetes cluster
sidebar_label: TCID-DIR-OP-DEVICE-VIEW-SCALE-RESTART
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
    <td> TCID-DIR-OP-DEVICE-VIEW-SCALE-RESTART </td>
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
  - Availability of 20 or more disks per node is recommended

### Observations
- K8s cluster has undergone various restarts over a period of time
  - In some cases, nodes were rebooted
  - In some other cases, few OpenEBS pods were restarted

### Expectations
- Users should be able to list devices attached to this K8s cluster
- Users should be able to categorize device types e.g. HDD, SSD, etc
- Users should be able to identify devices categorized by nodes

### Notes to the Reviewer
- This is a **negative** test case
- Recent versions of K8s & DOP needs to be used

### Test Result Link

- https://github.com/mayadata-io/oep-e2e-results/tree/master/TCID-DIR-OP-DEVICE-VIEW-SCALE-RESTART