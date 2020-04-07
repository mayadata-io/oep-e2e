---
id: TC-Team-RoleChange
title: Teaming Role Change
sidebar_label: TC-Team-RoleChange
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
    <td> TCID-TRRC02 </td>
    <td> TC-Team-RoleChange </td>
    <td> Teaming </td>
    <td> Role Change Functionality </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed
- Project owner pouser1


### Test Case Info
- Check the Invite user functionality works fine.

### User Action

- Login as pouser1
  - Change pruser1 as projectAdmin, then to project Member and then back to project Readonly
- Login as pauser1
  - Change pruser1 as project Admin, then to project Member and then back to project Readonly


### Expected Results

- Role change of pruser1 should be changed to Admin, then to project member and then back to readonly
- Role change of pruser1 should be changed to Admin, then to project member and then back to readonly
