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



- - #### Local Authentication

| TCID                                   | TC Name | GCP               | Rancher | Konvoy | AWS  |
| -------------------------------------- | ------------------------- | ----------------- | ------- | ------ | ---- |
| [tcid-aula01](tc-auth-la-admin) | TC-Auth-LA-Admin | Y | W | W | W |
| [tcid-aula02](tc-auth-la-user)   | TC-Auth-LA-User | Y    | W       | W | W |
| [tcid-aula03](tc-auth-la-signup)     | TC-Auth-LA-Signup | Y              | W | W | W |

- #### Github Authentication

| TCID                                   | TC Name | GCP               | Rancher | Konvoy | AWS  |
| -------------------------------------- | ------------------------- | ----------------- | ------- | ------ | ---- |
| [tcid-augh02](tc-auth-github-user)   | TC-Auth-Github-User | Y    | W       | N | W |
| [tcid-augh03](tc-auth-github-signup)     | TC-Auth-Github-Signup | Y              | W | N | W |

- #### GMail Authentication

| TCID                                   | TC Name | GCP               | Rancher | Konvoy | AWS  |
| -------------------------------------- | ------------------------- | ----------------- | ------- | ------ | ---- |
| [tcid-augm02](tc-auth-gmail-user)   | TC-Auth-Gmail-User | Y    | N      | N | W |
| [tcid-augm03](tc-auth-gmail-signup)     | TC-Auth-Gmail-Signup | Y              | N | N | W |


- #### Active Directory


| TCID                                   | TC Name | GCP               | Rancher | Konvoy | AWS  |
| -------------------------------------- | ------------------------- | ----------------- | ------- | ------ | ---- |
| [tcid-augm02](tc-auth-ad-user)   | TC-Auth-Gmail-User | N   | W       | W | N |
| [tcid-augm03](tc-auth-ad-signup)     | TC-Auth-Gmail-Signup | N             | W | W | N |

