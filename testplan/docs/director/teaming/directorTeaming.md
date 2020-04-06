---
id: directorTeaming
title: Test plan for Director Teaming
sidebar_label: Test Strategy
---
------

This page captures the test scenarios for Teaming feature in Director. The following areas would be covered as part of teaming functionality
- Invite User
 - Project Account
 - Cluster Account
- Roles
  - Owner
  - Admin
  - Member
  - Read Only
- Role Change

## Teaming

- #### Invite Users

An account member can invite users, to manage with the scope of cluster level or project level. Project account can invite cluster/project account user but not vice-versa.


- #### Roles
There are 4 roles for an user as listed below with order of access level, where Owner is having the highest access.
  1.  Owner
  2.  Admin
  3.  Member
  4.  ReadOnly


- #### Role Change
  Role change can be done to a same or higher level. Where Owner is the highest and ReadOnly is the lowest level.
  
  | TCID                                       | TC Name                     | GCP  | Rancher | Konvoy | AWS  |
  | ------------------------------------------ | --------------------------- | ---- | ------- | ------ | ---- |
  | [tcid-triv01](TC-Team-InviteUser)          | TC-Teaming-InviteUser       | Y    | W       | W      | W    |
  | [tcid-trrc02](TC-Team-RoleChange)          | TC-Team-RoleChange          | Y    | W       | W      | W    |
  | [tcid-trrc03](TC-Team-RoleChange-Negative) | TC-Team-RoleChange-Negative | Y    | W       | W      | W    |


