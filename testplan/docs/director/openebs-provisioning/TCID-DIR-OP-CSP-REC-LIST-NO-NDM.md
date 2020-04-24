---
id: TCID-DIR-OP-CSP-REC-LIST-NO-NDM
title: List cstor pool recommendations without NDM
sidebar_label: TCID-DIR-OP-CSP-REC-LIST-NO-NDM
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
    <td> TCID-DIR-OP-CSP-REC-LIST-NO-NDM </td>
    <td> CStorPool Recommendation </td>
    <td> List Verification Without NDM </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed
- NDM should not be running

### Details
- Director version 1.9 onwards
- Negative test case

### Steps Performed in the test

- Invoke API to list recommendations
- Invoke API to get capacity based recommendations
- Invoke API to get device based recommendations

### Expected output

- Director should list the supported recommendations without error
- Director should list the capacity based recommendations without error
- Director should list the device based recommendations without error

NOTE: Director may show nil list if there are no BlockDevices
