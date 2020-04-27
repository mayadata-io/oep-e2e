---
id: authentication
title: Director Authentication
sidebar_label: Test Strategy
---
------

### Authentication
As a DevOps admin, I want my teams to access Director using existing authentication approaches as approved in my organisation. The roles and access set in the identity provider should be sufficient to access specific pages of Director. Users should not be asked to login repeatedly if the browser has already been authenticated. Users should be provided with appropriate messages in case of any failures during login. Users should not be able to access Director when their access are removed from respective identity provider.

I want support for following authentication methods:
- **Local Auth:** Credentials are validated against the identity stored in local database (MySQL) in Director.
- **Gitlab Auth:** Credentials are validated from Gitlab identity provider using Oauth. 
- **GMail Auth:** Credentials are validated from GMail identity provider using Oauth.
- **Active Directory Auth:** Credentials are validated against the identities available in Microsoft Active Directory using LDAP. 


### Scalability
As a DevOps admin, I want Director to support authentication to all the users across teams. I want Director to support authentication to at-least 30 teams where each team consist of 50 users. A team comprises of users having different authorizations.

### Performance
As a DevOps admin, I want Director to authentication users within 5 seconds with 100 simultaneous login attempts. These 100 simultaneous logins can be come from users with different authorizations.

### Security
As a DevOps admin, I want none of my teams to access Director, if these teams do not have access in organization's identity provider. This also implies teams that have access to Director do not inadvertently have access to resources that these teams do not have access to. 

### TestCase IDs

| TCID                                                    | Rancher | Konvoy | AWS  |
| ------------------------------------------------------- | ------- | ------ | ---- |
| [TCID-DIR-AUTH-LOCAL-ADMIN](TCID-DIR-AUTH-LOCAL-ADMIN)  |         |        |      |
| [TCID-DIR-AUTH-LOCAL-USER](TCID-DIR-AUTH-LOCAL-USER)    |         |        |      |
| [TCID-DIR-AUTH-LOCAL-PERF](TCID-DIR-AUTH-LOCAL-PERF)    |         |        |      |
| [TCID-DIR-AUTH-LOCAL-SCALE](TCID-DIR-AUTH-LOCAL-SCALE)  |         |        |      |
| [TCID-DIR-AUTH-GH-ADMIN](TCID-DIR-AUTH-GH-ADMIN)        |         |        |      |
| [TCID-DIR-AUTH-GH-USER](TCID-DIR-AUTH-GH-USER)          |         |        |      |
| [TCID-DIR-AUTH-GH-PERF](TCID-DIR-AUTH-GH-PERF)          |         |        |      |
| [TCID-DIR-AUTH-GH-SCALE](TCID-DIR-AUTH-GH-SCALE)        |         |        |      |
| [TCID-DIR-AUTH-GMAIL-ADMIN](TCID-DIR-AUTH-GMAIL-ADMIN)  |         |        |      |
| [TCID-DIR-AUTH-GMAIL-USER](TCID-DIR-AUTH-GMAIL-USER)    |         |        |      |
| [TCID-DIR-AUTH-GMAIL-PERF](TCID-DIR-AUTH-GMAIL-PERF)    |         |        |      |
| [TCID-DIR-AUTH-GMAIL-SCALE](TCID-DIR-AUTH-GMAIL-SCALE)  |         |        |      |
| [TCID-DIR-AUTH-AD-ADMIN](TCID-DIR-AUTH-AD-ADMIN)        |         |        |      |
| [TCID-DIR-AUTH-AD-USER](TCID-DIR-AUTH-AD-USER)          |         |        |      |
| [TCID-DIR-AUTH-AD-PERF](TCID-DIR-AUTH-AD-PERF)          |         |        |      |
| [TCID-DIR-AUTH-AD-SCALE](TCID-DIR-AUTH-AD-SCALE)        |         |        |      |
