---
id: TCID-DIR-OP-CSP-REC-LIST
title: List cstor pool recommendations
sidebar_label: TCID-DIR-OP-CSP-REC-LIST
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
    <td> TCID-DIR-OP-CSP-REC-LIST </td>
    <td> CStorPool Recommendation </td>
    <td> List Verification </td>
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

### Expected output

- Director should list the supported recommendations
- Director should list the capacity based recommendations
- Director should list the device based recommendations
