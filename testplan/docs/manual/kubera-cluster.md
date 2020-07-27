---
id: kubera-cluster
title: Kubera Manual Testing Cluster Connect
sidebar_label: Kubera cluster
---

### Below test cases are executed manully for cluster connect


#### To verify self connected cluster is shown for Admin user 
- The self connected cluster shown be show as active 

#### To verify self connected cluster should get disconnected 
- Cluster should get disconneted from UI and backend

#### To verify clusters can be connected using Admin account 
- The Cluster should be shown up in active state 

#### To verify clusters can be connected using local auth 
- The Cluster should be shown up in active state 

#### To Verify that connecting link is getting generated for respective platform.
- URL link should get generated 

#### To verify cluster name should not be less than 5 character and should not contain any special character 
- Error message should be shown in UI.
- Once proper cluster name is provided the URL link pop should get generated. 

#### To verify cluster disconnect functionality 
- Cluster should get disconneted from UI.
- From backend maya-system namespace should get cleaned up. 






