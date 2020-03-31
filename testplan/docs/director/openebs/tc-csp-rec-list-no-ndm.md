---
id: tc-csp-rec-list-no-ndm
title: List cstor pool recommendations
sidebar_label: tc-csp-rec-list-no-ndm
---
------

### Experiment Metadata

<table>
  <tr>
    <th> TCID </th>
    <th> TCNAME </th>
    <th> Type </th>
    <th> Description </th>
  </tr>
  <tr>
    <td> tcid-csprec002 </td>
    <td> tc-csp-rec-list-no-ndm </td>
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

### Steps Performed in the test

- Invoke API to list recommendations
- Invoke API to get capacity based recommendations
- Invoke API to get device based recommendations

### Expected output

- Director should list the supported recommendations without error
- Director should list the capacity based recommendations without error
- Director should list the device based recommendations without error

NOTE: Director may show nil list if there are no BlockDevices
