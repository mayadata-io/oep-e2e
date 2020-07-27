---
id: kubera-dmaas
title: Kubera Manual Testing DMaas
sidebar_label: Kubera dmaas
---

### Below test cases are executed manully for dmaas


#### Create dmaas schedule and check the status for deployment app(cstor) 
- schedule should get created successfully 

#### Create a dmaas schedule and check the status for statefulset app(cstor) 
- schedule should get created successfully 

#### Check the status backups 
- Schedule should become active.
- Clicking on schedule should sbow backup status as completed.
- Due to some issues backups can be partially failed also. 

#### Check if the backups are taken incrementaly(Full backup should also be checked in case of cstor based backup) 
- Backups should be completed for specificed time period and data should be present 

#### Start a restore of chosen backup 
- Application should get restored to the destination cluster.
- If the restores failed then proper error message should be shown 

#### Try to delete schedule 
- The respective schedule should get deleted 

#### Create dmaas schedule and check the status for deployment app(LocalPV)
- schedule should get created successfully 

#### Create dmaas schedule and check the status for statefulset app(LocalPV)
- schedule should get created successfully

#### Create dmaas schedule and check the status for deployment app(Jiva-default)
- schedule should get created successfully 

#### Create dmaas schedule and check the status for statefulset app(Jiva-default)
- schedule should get created successfully 

#### Create dmaas schedule and check the status for deployment app which is having non-openebs volume like nfs volumes
- schedule should get created successfully 

#### Start a restore of chosen backup for non openebs volume
- Application should get restored to the destination cluster.
- If the restores failed then proper error message should be shown 

#### Create dmaas schedule for stateless application
- schedule should get created successfully 

#### Start a restore of chosen backup for stateless application
- Application should get restored to the destination cluster.
- If the restores failed then proper error message should be shown 



