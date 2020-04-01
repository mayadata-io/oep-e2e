---
id: tc-auth-gmail-user
title: GMail Auth user
sidebar_label: TC-Auth-GMail-User
---
------


## GMail Authentication User

### Experiment Metadata

<table>
  <tr>
    <th> TCID </th>
    <th> TCNAME </th>
    <th> Type </th>
    <th> Description </th>
  </tr>
  <tr>
    <td> TCID-augm02 </td>
    <td> TC-Auth-Gmail-User </td>
    <td> GMail Authentication </td>
    <td> User verification </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed


### Details
- Check the login for GMail user1@gmail.com

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

