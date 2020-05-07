---
id: TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-MIRROR
title: Create mirror cstor pool cluster
sidebar_label: TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-MIRROR
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
    <td> TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-MIRROR </td>
    <td> CStorPool Recommendation </td>
    <td> Verify creation of mirror cstor pool cluster </td>
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
- Invoke API to get mirror based cstor pool recommendations
- Invoke API to create mirror cstor pool cluster

### Expected output

- Director should be able to create mirror cstor pool cluster

### Test Result Link

- https://github.com/mayadata-io/oep-e2e-results/tree/master/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-CREATE-MIRROR
