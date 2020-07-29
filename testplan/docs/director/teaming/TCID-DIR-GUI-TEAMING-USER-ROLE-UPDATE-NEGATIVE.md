---
id: TCID-DIR-GUI-TEAMING-USER-ROLE-UPDATE-NEGATIVE
title: Teaming Role Change negative
sidebar_label: TCID-DIR-GUI-TEAMING-USER-ROLE-UPDATE-NEGATIVE
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
    <td> TCID-DIR-GUI-TEAMING-USER-ROLE-UPDATE-NEGATIVE </td>
    <td> TCID-DIR-GUI-TEAMING-USER-ROLE-UPDATE-NEGATIVE </td>
    <td> Teaming </td>
    <td> Non permissive Role Change Functionality  </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed
- Project owner pouser1


### Details
- Other then project owner are not allowed to change role of users in a project.

### Steps Performed in the test

- Login as project owner(pouser1).
- Invite already sign up users into project as project member, admin, read admin roles.
- Logout from project owner account.
- Login as member or admin or read admin.
- Accept the received invitation.
- Try to change the role of existing user in a project.


### Expected output

- Role change by project member user should fail.
- Role change project readonly user should fail.
- Role change by project admin user should fail.


### Test Result Link

- https://github.com/mayadata-io/oep-e2e-results/tree/master/TCID-DIR-GUI-TEAMING-USER-ROLE-UPDATE-NEGATIVE