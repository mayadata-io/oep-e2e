---
id: tcid-aula03
title: Local Auth Non Admin user Signup
sidebar_label: TC-LA-Signup
---
------


### Experiment Metadata

<table>
  <tr>
    <th> TCID </th>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> TCID-aula03 </td>
    <td> Local Authentication </td>
    <td> Signup verification </td>
    <td> ALL </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed
- TC id tcid-lau01 and tcid-lau02 should be executed


### Details
- Check the Signup with signuser1

### Steps Performed in the test

- Signup for a new user signuser1
- Check for user name 
  - create with user1 
  - boundary value (min length)
  - boundary value (max length)
- Password validity check
  - Check for min char length (8 chars)
  - Check for complexity 
- email check should be unique
- User should be enabled
- Update profile


### Expected output

- Able to login with required profile updated.
- User name checks
  - create with user1 (It should fail as user1 exists)
- Passowrd checks
  - should pass (complexity should match)
- email checks
  - should pass (no duplicate should work)
- User should be able to login
- Update profile fields

