---
id: kubera-teaming
title: Kubera Manual Testing Teaming 
sidebar_label: Kubera teaming
---

### Below test cases are executed manully for teaming 


#### ProjectOwner can invite others in his/her Project. 
- Invitation should be send to the invitee 

#### To view pending invites 
- Users who have not accepted the invite can be viewed 

#### Only invitee can accept or reject invitation  
- Accept or Decline request can be seen in invitation page 

#### Validate invitation reject process 
- The status to the inviter will be shown as rejected 

#### Validate invitation accept process 
- From manage project dashboard he/she can see the project the user is part of.(invited user dashboard)
- Inviter can view that user in All user tab

#### Project owner can only change the member role 
- Role of invited user can be changed successfully

#### To verify Project Owner access 
- Can invite others to his project.
- Can change the role of the member in his project.
- Can delete a member from a project.

#### To verify Project Admin access 
- Can connect or disconnect clusters
- Can manage alerts 
- can upgrade cluster
- Can create dmaas schedules
- Can restore any backups

#### To verify Project Read Admin access
- Connect cluster button on cluster page should be invisible
- Cannot perform openEBS upgrade

#### To verify Project  Member access
- Restricted user, no access
- In manage project(project page), project should not be clickable

#### Non Project owner can not change the member role
- Role of invited user can not  be changed

#### To check that no console error is shown 
- No console error is shown during accepting of invitation







