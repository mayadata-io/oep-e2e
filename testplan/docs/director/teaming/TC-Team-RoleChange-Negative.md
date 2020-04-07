---
id: TC-Team-RoleChange-Negative
title: Teaming Role Change
sidebar_label: TC-Team-RoleChange-Negative
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
    <td> TCID-TRRC03 </td>
    <td> TC-Team-RoleChange-Negative </td>
    <td> Teaming </td>
    <td> Non permissive Role Change Functionality  </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed
- Project owner pouser1


### Details
- Check the Invite user functionality works fine.

### Steps Performed in the test

- Login as pouser1
  - Change pruser1 as project owner (self)
- Login as pauser1
  - Change pouser1 as project admin (self), then project owner
- Login as pmuser1
  - Change pouser1 as project member (self), then to project owner, then to project admin, then to project readonly
- Login as pruser1
  - Change pouser1 as project readonly (self), then to project owner, then to project admin, then to project member


### Expected output

- Role change should fail for all combination
- Role change should fail for all combination
- Role change should fail for all combination
- Role change should fail for all combination
