---
id: TCID-DIR-TEAMING-USER-ROLE-UPDATE
title: Teaming Role Change
sidebar_label: TCID-DIR-TEAMING-USER-ROLE-UPDATE
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
    <td> TCID-DIR-TEAMING-USER-ROLE-UPDATE </td>
    <td> TCID-DIR-TEAMING-USER-ROLE-UPDATE </td>
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

- Login as project owner(pouser1).
- Invite already sign up users into project as project member, admin, read admin roles.
- Login as invited user and accept invitation.
- Login as project owner
- Change user roles of the users in a project.


### Expected Results

- Role chnage by project owner of user to ProjectAdmin from ProjectMember should happen
- Role chnage by project owner of user to ProjectAdmin from ProjectReadAdmin should happen
- Role chnage by project owner of user to ProjectMember from ProjectAdmin should happen
- Role chnage by project owner of user to ProjectMember from ProjectReadAdmin should happen
- Role chnage by project owner of user to ProjectReadAdmin from ProjectAdmin should happen
- Role chnage by project owner of user to ProjectReadAdmin from ProjectMember should happen

### Test Result Link

- https://github.com/mayadata-io/oep-e2e-results/tree/master/TCID-DIR-TEAMING-USER-ROLE-UPDATE