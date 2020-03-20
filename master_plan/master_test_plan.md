## Test Plan Template:

Director OnPrem

### Prepared by:

Prabhat kumar 

Date: 19/03/2020

## TABLE OF CONTENTS

### 1.0 INTRODUCTION

### 2.0	OBJECTIVES AND TASKS 

#### 2.1	Objectives 
#### 2.2	Tasks 

### 3.0 SCOPE

### 4.0	Testing Strategy 

#### 4.1	Alpha Testing (Unit Testing) 
#### 4.2	System and Integration Testing 
#### 4.3	Performance and Stress Testing 
#### 4.4	User Acceptance Testing 
#### 4.5	Batch Testing 
#### 4.6	Automated Regression Testing 

### 5.0 Hardware Requirements

### 6.0	Environment Requirements 

#### 6.1	Main Frame 
#### 6.2	Workstation 

### 7.0 Test Schedule

### 8.0 Control Procedures

### 9.0 Features to Be Tested

### 10.0 Features Not to Be Tested
 
### 11.0 Resources/Roles & Responsibilities

### 12.0 Schedules

### 13.0 Significantly Impacted Departments (SIDs)

### 14.0 Dependencies

### 15.0 Risks/Assumptions

### 16.0 Tools

### 17.0	Approvals 


### 1.0 Introduction:
DirectorOnline, as well as Director OnPrem, helps us quickly view multi-cloud Kubernetes resources from a single console, helps in troubleshooting, monitoring stateful applications, access logs of applications at a central location, take a backup of applications, etc.
So, the features are the same for both Online as well as On-Premise version the only difference lies in the administration.

### 2.0 Objectives and tasks

#### 2.1 Objectives:
The objective should be to cover all the areas of DOP testing such as Authentication, Installation, cluster connect etc. 

#### 2.2 Tasks:
a. Test the DOP product(features and functionality) on every release.              
b. DOP testing should be done using E2E automation.                    
c. Manual testing will be require if E2E is not covered for any specfic feature or functionality.           
d. Once testing is done file issues for the bug.                                        
e. Set priority level for bug fixes for next release.    

### 3.0 Scope:

#### General:
There are different features and functionality of DOP that are tested. Listing them below.
a. Authentication.                        
b. Browser                          
c. Profile                                         
d. connect cluster                                                                      
e. Dashboard                                                                                 
f. Scope                                         
e. Metrics                                                          
f. Alerts                                                  
g. Dmaas                                                    
h. Teaming                                                       
i. upgrade                                                                          
j. OpenEBS installation                                             
etc

#### Tactics:
a.To get the build from Director team.                                                    
b. Install DOP on any cluster.                                                                     
c. Verify the installation part automated/manually.                                       
d. Verify the different features and functionality manually for the onces which had not been automated.             
e. End Goal is to have to e2e pipeline running for the new features and later on cover the existing features in E2E pipeline.

### 4.0 Testing statergy:
a. To verify the DOP installation should be smooth across different OnPrem clusters such as Kubeadm,konvoy, Rancher, Openshift etc.   
b. For installation of DOP cstor storage class should be used for the pvc(mysql,cassandra,elasticsearch,grafana and mayastore)        
c. After installation of DOP UI should be accessible.                              
d. Verify the authentication functionality of DOP. The Main focus area should be Local authentication.                             
e. Verify that UI should be accessible in chrome,firefox and safari.                                           
f. Verify that self connected cluster are shown in Administrator account.                                                   
g. Verify the cluster connect and disconnect functionality.                                                          
h. Verify all the dashboards are showing the graphs or data.                                        
i. Metrics are shown for volumes and pools.                                                        
j. Alerts are getting generated at cluster level.                                                          
k. Verify the teaming functionality.                                                                                             
l. Verify the dmaas functionality. Cover all the 3 providers (GCP,AWS and Minio)                                   
m. verify the OpenEBS installation functionality.                                                               
n. Verify the OpenEBS upgrade functionality.                  
















 





























