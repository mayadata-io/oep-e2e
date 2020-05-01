---
id: TCID-DIR-OP-CSTOR-POOL-RECOMMEND-MIRROR-REBOOT-NODE
title: Verify mirror cstor pool cluster after node reboot
sidebar_label: TCID-DIR-OP-CSTOR-POOL-RECOMMEND-MIRROR-REBOOT-NODE
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
    <td> TCID-DIR-OP-CSTOR-POOL-RECOMMEND-MIRROR-REBOOT-NODE </td>
    <td> Verify mirror cstor pool cluster after node reboot </td>
    <td> Verify creation of mirror cstor pool cluster </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed

### Details
- Director version 1.9 onwards
- Positive test case

### Steps Performed in the test

- Invoke API to list recommendations
- Invoke API to get capacity based recommendations
- Invoke API to get device based recommendations
- Invoke API to get mirror based cstor pool recommendations
- Invoke API to create mirror cstor pool cluster
- Reboot node and check status of pools 

### Expected output

- The status of pools should be Active
