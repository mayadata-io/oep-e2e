---
id: kubera-authentication
title: Kubera Manual Testing Authentication
sidebar_label: Kubera authentication
---

### Below test cases are executed manully for authentication


#### To verify Administrator Login
- Administrator should be able to login using credentials

#### To verify the Change password functionality for Administrator account
- Administrator should be able to login once password had been changed


#### To verify signup functionality in Local Auth 
- Using Local Auth any user can signup to Kubera Director OnPrem


#### To verify the Change password functionality for local auth account 
- Local Auth user should be able to login once password had been changed


#### To verify error message is shown if wrong password is provided 
- Error message should be shown that either username or password is incorrect


#### To verify error message is shown if wrong email id is provided 
- Error message should be shown that either username or password is incorrect 

#### Password for local authentication should be alpha numeric supported
- Error message should be shown that password must be alpha numeric with atleast 8 chars and utmost 20 chars
- Once the correct format of password is provided signup/login should be successful

#### To verify unique Email ID for each user
- Error message should be shown that this email id is already been taken
- Once unique email Id is provided signup should be successful





