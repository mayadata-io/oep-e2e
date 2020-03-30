---
id: tcid-aula01
title: Local Auth Admin user
sidebar_label: LA Admin
---
------


### Local Authentication Admin User

### Experiment Metadata

<table>
  <tr>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> Local Authentication </td>
    <td> Admin user verification </td>
    <td> ALL </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed


### Details
- Check the login for Admin user 

### Steps Performed in the test

- Login using Administrator user

- Create 2 new users
  - user1
  - user2
- Enable user1

- Disable user2

- Login with wrong password

- Logout

- Change password

- Time out

- Update profile

### Expected output

- Able to login
- Able to create users
- Able to login with user1
- Unable to login with user2
- Unable to login with wrong password
- Logout, then on access it should ask for login
- Timeout, on an time out it should logout and ask for re-login
- Update profile fields

