---
id: TC-Team-InviteUser
title: Teaming Invite User
sidebar_label: TC-Team-InviteUser
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
    <td> TCID-TRIV01 </td>
    <td> TC-Team-InviteUser </td>
    <td> Teaming </td>
    <td> Invite User Functionality </td>
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
- Invite pauser1 as project Admin
- Invite pruser1 as project Read Only
- Invite pmuser1 as project Member
- Login as the above user and verify the functionality


### Expected output

- Invitation should be sent to all users
- pauser1 should be joined as project Admin, user should have all project access
- pruser1 should be joined as Readonly, no write operation can be performed
- pmuser1 should be joined as project member, user should have write permission, but will not have admin powers like disabling user etc.
