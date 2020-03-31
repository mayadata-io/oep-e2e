---
id: tcid-augm03
title: GMail Auth user Signup
sidebar_label: TC-GMail-Signup
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
    <td> TCID-augm03 </td>
    <td> GMail Authentication </td>
    <td> Signup verification </td>
    <td> ALL </td>
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

