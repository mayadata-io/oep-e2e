---
id: directorAuth
title: Director Authentication
sidebar_label: Test Strategy
---
------

## Authentication
This page captures the test scenarios for Authentication methods supported in DOP(Director Onprem). DOP supports the following authentication methods against various Identity providers
- **Local Auth:** Credentials are validated against the Identity stored local database (MySQL) in Director.
- **Gitlab Auth:** Credentials are validated from Gitlab Identity provider using Oauth. 
- **GMail Auth:** Credentials are validated from GMail Identity provider using Oauth.
- **Active Directory Auth:** Credentials are validated against the Identities in Microsoft Active Directory using LDAP. 

Test cases covered for the all the above authentication methods are as mentioned below,
- Admin Authentication - Admin will have option to enable and disable users. This will be available for Local Auth and AD Auth only.
- User Authentication - Regular users will have access to the portal. They will different roles based on teaming. Roles and access control will be covered in [Teaming](/docs/director/teaming/directorTeaming)
- Signup Feature
- Password Complexity check
- Profile field validation
  - Username field validations. First name, Last name, Boundary condition for  min, max chars, unique identity, case sensitive
  - email field validation. Type validation, unique identity
  - Roles (optional)
  - Company (optional)
  - Phone (optional)
  - Profile status updation


- #### Local Authentication

| TCID                                                   | Brief Description         | #Issue | Platform |
| ------------------------------------------------------ | ----------------------- - | ------ | -------- |
| <a href="tcid-aula01" target="_blank">Admin Auth</a>   | Admin User authentication |        | All      |
| <a href="tcid-aula02" target="_blank">User Auth</a>    | User authentication       |        | All      |
| <a href="tcid-aula03" target="_blank">Sign up</a>      | Signup Functionality      |        | All      |

- #### Github Authentication

| TCID                                                   | Brief Description      | #Issue | Platform |
| ------------------------------------------------------ | ---------------------- | ------ | -------- |
| <a href="tcid-augi02" target="_blank">User Auth</a>    | User authentication    |        | All      |
| <a href="tcid-augi03" target="_blank">Sign up</a>      | Signup Functionality   |        | All      |


- #### GMail Authentication

| TCID                                                   | Brief Description      | #Issue | Platform |
| ------------------------------------------------------ | ---------------------- | ------ | -------- |
| <a href="tcid-augm02" target="_blank">User Auth</a>    | User authentication    |        | All      |
| <a href="tcid-augm03" target="_blank">Sign up</a>      | Signup Functionality   |        | All      |

- #### Active Directory

| TCID                                                   | Brief Description      | #Issue | Platform |
| ------------------------------------------------------ | ---------------------- | ------ | -------- |
| <a href="tcid-auad02" target="_blank">User Auth</a>    | User authentication    |        | All      |
| <a href="tcid-auad03" target="_blank">Sign up</a>      | Signup Functionality   |        | All      |

