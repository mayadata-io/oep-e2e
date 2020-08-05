---
id: TCID-DIR-OP-OPENEBS-UPGRADE-CP
title: Upgrade openebs control plane components
sidebar_label: TCID-DIR-OP-OPENEBS-UPGRADE-CP
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
    <td> TCID-DIR-OP-OPENEBS-UPGRADE-CP </td>
    <td> Upgrade openebs </td>
    <td> Upgrade openebs control plane components using director </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed

### Details
- Director version 1.9 onwards
- Positive test case

### Steps Performed in the test

- Invoke API to install openebs.
- Invoke API to upgrade openebs control plane components.
- Invoke API to check job status.

### Expected output

- Director should be able to upgrade openebs control plane components.

### Test Result Link

- https://github.com/mayadata-io/oep-e2e-results/tree/master/TCID-DIR-OP-OPENEBS-UPGRADE-CP