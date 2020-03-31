---
id: tcid-augi02
title: Github Auth user
sidebar_label: Github User
---
------


## Github Authentication User

### Experiment Metadata

<table>
  <tr>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> Github Authentication </td>
    <td> User verification </td>
    <td> ALL </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed


### Details
- Check the login for Github user1 

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

