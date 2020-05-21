---
id: TCID-DIR-OP-RE-INSTALL-OPENEBS
title: Install OpenEBS on a machine already OpenEBS is installed with same version using operator
sidebar_label: TCID-DIR-OP-RE-INSTALL-OPENEBS
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
    <td> TCID-DIR-OP-RE-INSTALL-OPENEBS </td>
    <td> Install openebs </td>
    <td> Install OpenEBS on a machine already OpenEBS is installed with same version using operator </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed

### Details
- Director version 1.9 onwards
- Negative test case

### Steps Performed in the test

- Invoke API to list openbses entry.
- Invoke API to install openebs .
- Invoke API to check job status .

### Expected output

- At the time of reinstalling openebs using director it should give error.