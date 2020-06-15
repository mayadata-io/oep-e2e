---
id: TCID-DIR-OP-INSTALL-OPENEBS-DP-ON-SPECIFIC-NODE
title: Install openebs data plane on specific node using director
sidebar_label: TCID-DIR-OP-INSTALL-OPENEBS-DP-ON-SPECIFIC-NODE
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
    <td> TCID-DIR-OP-INSTALL-OPENEBS-DP-ON-SPECIFIC-NODE </td>
    <td> Install openebs </td>
    <td> Install openebs data plane on specific node using director </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed

### Details
- Director version 1.9 onwards
- Positive test case

### Steps Performed in the test

- Invoke API to list openebses entry.
- Invoke API to install openebs .
- Invoke API to check job status .

### Expected output

- Director should be able to install openebs data plane components in particular node.

### Test Result Link

- https://github.com/mayadata-io/oep-e2e-results/tree/master/TCID-DIR-OP-INSTALL-OPENEBS-DP-ON-SPECIFIC-NODE