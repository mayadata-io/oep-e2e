---
id: TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-RAIDZ
title: Create raidz cstor pool cluster
sidebar_label: TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-RAIDZ
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
    <td> TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-RAIDZ </td>
    <td> CStorPool Recommendation </td>
    <td> Verify creation of raidz cstor pool cluster </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed
- BlockDevices should be detected by NDM

### Details
- Director version 1.9 onwards
- Positive test case

### Steps Performed in the test

- Invoke API to list recommendations
- Invoke API to get capacity based recommendations
- Invoke API to get device based recommendations
- Invoke API to get raidz based cstor pool recommendations
- Invoke API to create raidz cstor pool cluster

### Expected output

- Director should be able to create raidz cstor pool cluster
