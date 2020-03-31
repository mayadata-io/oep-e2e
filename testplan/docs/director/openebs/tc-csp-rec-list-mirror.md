---
id: tc-csp-rec-list-mirror
title: List stripe based cstor pool recommendations
sidebar_label: tc-csp-rec-list-mirror
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
    <td> tcid-csprec003 </td>
    <td> tc-csp-rec-list-mirror </td>
    <td> CStorPool Recommendation </td>
    <td> Verify List of Mirror Recommendations </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed
- BlockDevices should be detected by NDM

### Details
- Director version 1.9 onwards

### Steps Performed in the test

- Invoke API to list recommendations
- Invoke API to get capacity based recommendations
- Invoke API to get device based recommendations
- Invoke API to get mirror based cstor pool recommendations

### Expected output

- Director should list mirror based cstor pool recommendations
