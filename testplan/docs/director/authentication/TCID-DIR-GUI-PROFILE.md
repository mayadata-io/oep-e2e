---
id: TCID-DIR-GUI-PROFILE
title: Profiile
sidebar_label: TCID-DIR-GUI-PROFILE
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
    <td>TCID-DIR-GUI-PROFILE</td>
    <td> Profile</td>
    <td> User profile </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed and accessible from browser


### Details
- User profile completion and profile update.

### Steps Performed in the test
- Verify profile can be updated just after signup
- Verify the profile info is same as whatever provided during onboarding time
- Verify first and last name can be modified for local Auth user
- Verify company,Role and phone can be modified for local Auth user
- Verify First and last Name cannot be modified for local Auth Admin user
- Verify Email id  can be modified for any user

### Expected output
- Profile can be updated just after signup
- Profile info is same as whatever provided during onboarding time
- First and last name can be modified for local Auth user
- Company,Role and phone can be modified for local Auth user
- First and last Name cannot be modified for local Auth Admin user
- Email id  can be modified for any user

### Test Result Link

- https://github.com/mayadata-io/oep-e2e-results/tree/master/TCID-DIR-GUI-PROFILE
