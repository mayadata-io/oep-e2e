---
id: TCID-DIR-TEAMING-USER-INVITE
title: Teaming Invite User
sidebar_label: TCID-DIR-TEAMING-USER-INVITE
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
    <td> TCID-DIR-TEAMING-USER-INVITE </td>
    <td> TCID-DIR-TEAMING-USER-INVITE </td>
    <td> Teaming </td>
    <td> Invite User Functionality </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed
- Project owner pouser1


### Testcase Info
- Check the Invite user functionality works fine.

### User Actions

- Login as pouser1
- Invite pauser1 as project Admin
- Invite pruser1 as project Read Only
- Invite pmuser1 as project Member
- Login as the above user and accept the received invitation


### Expected Results

- Invitation should be sent to all users
- pauser1 should be joined as project Admin, user should have all project access
- pruser1 should be joined as Readonly, no write operation can be performed
- pmuser1 should be joined as project member, user will be part of the project but no access to resources.
