---
id: tc-auth-la-user
title: Local Auth Non Admin user
sidebar_label: TC-Auth-LA-User
---
------


## Local Authentication Normal User (Non Admin)

### Experiment Metadata

<table>
  <tr>
    <th> TCID </th>
    <th> TCNAME </th>
    <th> Type </th>
    <th> Description </th>
  </tr>
  <tr>
    <td> TCID-aula02 </td>
    <td> TC-Auth-LA-User </td>
    <td> Local Authentication </td>
    <td> Non Admin user verification </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed


### Details
- Check the login for user1 

### Steps Performed in the test

- Login using user1
- Enable user1
- Disable user1
- Login with wrong password
- Logout
- Change password
- Time out
- Update profile


### Expected output

- Able to login
- Unable to change the enable setting
- Unable to change the disable setting
- Unable to login with wrong password
- Logout, then on access it should ask for login
- Timeout, on an time out it should logout and ask for re-login
- Update profile fields

