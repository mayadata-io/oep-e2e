---
id: tc-auth-github-signup
title: Github Auth user Signup
sidebar_label:  TC-Auth-Github-Signup
---
------

## Github Authentication User Signup

### Experiment Metadata

<table>
  <tr>
    <th> TCID </th>
    <th> TCNAME </th>
    <th> Type </th>
    <th> Description </th>
  </tr>
  <tr>
    <td> TCID-augh03 </td>
    <td> TC-Auth-Github-Signup </td>
    <td> Github Authentication </td>
    <td> Signup verification </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed
- TC id tcid-laffu01 and tcid-lau02 should be executed


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

