---
id: TCID-DIR-OP-INSTALL-OPENEBS-CP-ON-SPECIFIC-NODE
title: Install openebs control plane on specific node using director
sidebar_label: TCID-DIR-OP-INSTALL-OPENEBS-CP-ON-SPECIFIC-NODE
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
    <td> TCID-DIR-OP-INSTALL-OPENEBS-CP-ON-SPECIFIC-NODE </td>
    <td> Install openebs </td>
    <td> Install openebs control plane on specific node using director </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed

### Details
- Director version 1.9 onwards
- Positive test case

### Steps Performed in the test

- Invoke API to list openbses entry.
- Invoke API to install openebs .
- Invoke API to check job status .

### Expected output

- Director should be able to install openebs control plane components in particular node.