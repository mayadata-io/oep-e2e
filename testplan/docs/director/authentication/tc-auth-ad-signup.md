---
id: tc-auth-ad-signup
title: Active Directory Auth user Signup
sidebar_label: TC-Auth-AD-Signup
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
    <td> TCID-auad03 </td>
    <td> TC-Auth-AD-Signup </td>
    <td> AD Authentication </td>
    <td> Signup verification </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed
- TC id tcid-auad02 should be executed
- AD access should be setup


### Details
- Check the Signup with signuser1

### Steps Performed in the test

- Signup for a new user signuser1
- Check for user name 
  - create with user1 
- email check should be unique
- User should be enabled
- Update profile


### Expected output

- Able to login with required profile updated.
- User name checks
  - create with user1 (It should fail as user1 exists)
- email checks
  - should pass (no duplicate should work)
- User should be able to login
- Update profile fields

