---
id: TCID-DIR-GUI-AUTH
title: Authentication
sidebar_label: TCID-DIR-GUI-AUTH
---
------

### Experiment Metadata

<table>
  <tr>
    <th> TCID </th>
    <th> Type </th>
    <th> Description </th>
  </tr>
  <tr>
    <td> TCID-DIR-GUI-AUTH </td>
    <td> Authentication </td>
    <td> Local User Authentication </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed and accessible from browser

### Details
- To verify signup functionality for Local Auth
- To verify error message is shown if wrong password is provided
- To verify error message is shown if wrong email ID is provided
- To verify password for local authentication should be alpha numeric supported
- To verify unique Email ID for each user
- To verify the Change password functionality for local auth account

### Steps Performed in the test
- Signup for Local Auth account
- Verify error message when wrong password entered
- Verify error message when wrong email ID entered
- Verify password for local authentication , it should be alpha numeric
- Verify unique Email ID for each user
- Verify the Change password for local auth account

### Expected output
- Signup for Local Auth account should be successful
- Error message should be displayed when wrong password entered
- Error message should be displayed when wrong email ID entered
- Password shoild only accept alpha numeric characters
- Unique Email ID for every user should be provided.
- Change password for local auth account should be successful.

### Test Result Link

- https://github.com/mayadata-io/oep-e2e-results/tree/master/TCID-DIR-GUI-AUTH
