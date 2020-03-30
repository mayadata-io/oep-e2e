---
id: tcid-aula02
title: Local Auth Non Admin user
sidebar_label: LA Non Admin User
---
------


## Local Authentication Normal User (Non Admin)

### Experiment Metadata

<table>
  <tr>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> Local Authentication </td>
    <td> Non Admin user verification </td>
    <td> ALL </td>
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

