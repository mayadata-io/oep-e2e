---
id: tc-auth-ad-user
title: Active Directory Auth user
sidebar_label: TC-Auth-AD-User
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
    <td> TCID-auad02 </td>
    <td> TC-Auth-AD-User </td>
    <td> AD Authentication </td>
    <td> User verification </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed
- AD access should be configured


### Details
- Check the login for AD user1 

### Steps Performed in the test

- Login using user1
- Logout
- Time out
- Update profile


### Expected output

- Able to login
- Logout, then on access it should ask for login
- Timeout, on an time out it should logout and ask for re-login
- Update profile fields

