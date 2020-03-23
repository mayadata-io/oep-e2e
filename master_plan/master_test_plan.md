## Test Plan Template:

Director OnPrem

## TABLE OF CONTENTS

### 1.0 INTRODUCTION

### 2.0	OBJECTIVES AND TASKS 

#### 2.1	Objectives 
#### 2.2	Tasks 

### 3.0 SCOPE

### 4.0	Testing Strategy 

#### 4.1	Sanity Testing  
#### 4.2	Performance and Stress Testing 
#### 4.3	Compatibilty Testing
#### 4.4	Regression Testing 
#### 4.5	API integration Testing
#### 4.6 Functional Testing

### 5.0 Test Schedule

### 6.0 Features to Be Tested

### 7.0 Features Not to Be Tested
 
### 8.0 Test execution cycle

### 9.0 Correlation between testing cycles and release plan

### 10.0 Test budgets according to project or overall operational budget

### 11.0 Interrelation between other departments and testing team

### 12.0 Risks associated with test project

### 13.0 Management and control of testing

### 14.0 Roles and responsibilities

### 15.0 Inputs and outputs for each test level

### 16.0	Approvals 


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
There are different features and functionality of DOP that needed to be tested. Listing them below.                             
a. Authentication.                        
b. Browser                          
c. Profile                                         
d. connect cluster                                                                      
e. Dashboard                                                                                 
f. Topology                                                                                                                  
e. Metrics                                                          
f. Alerts                                                  
g. Dmaas                                                    
h. Teaming                                                       
i. upgrade                                                                          
j. OpenEBS installation                                             
k. DOP upgrade
etc

#### List of items that will not be tested.                                          
a. The IOPS,thorughput,latency etc values that are shown in graphs are not tested means the values shown in graph is right or wrong.    
b. Exact error in the logs are not tested. We are not veryfing that whether we are getting exact logs with correct timestamp.
c. Cross-cloud-monitoring graphs values are not verified.

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

#### 4.1 Sanity Testing
a. DOP installation should be smooth. All the required images should be present in mayadata.
b. Signup and signin should happen for local Auth.
c. Cluster connect/disconnect check.
d. All the links should be working fine.
e. All the dashboards should show respectives info.


#### 4.2 Performance and stress testing:
a. Login to DOP from 500 browsers sessions.                                     
b. Connect clusters having 200 nodes.             
c. Connected cluster should have more than 50 Applications.                  

#### 4.3 Compatibilty testing:                 
a. Browsers(Chrome,firefox,safari).                                   
b. Platforms(Rancher,Kubeadm,kubespray,Konvoy,Openshit, etc).                               
c. Operating system(ubuntu 16.04 and other versions, Centos7.x,RancherOS, MicroOS, etc).
d. Different platform and operating system versions should also be considered.

#### 4.4	Regression Testing:

To make sure all the features which was working in previous release should not break with the intorduction of new features in new release.

#### 4.5 API Intergration testing.
TO DO

#### Functional Testing.
In functional testing we should test each of the functionality of DOP such as authentication,cluster connect etc. Have created a directory for functional testing. We add the content in it.

### 5.0 Test schedule.
OpenEBS control plane upgrade- 1.9                       
cstor pool provisioning - 1.9                                                                
Extend E2E to konvoy - 1.9                                                              
Extend E2E to Rancher - 1.9                                                          
Selinium based automation(for couple of TCs) - 1.9

### 6.0 Features to be tested:
a. OpenEBS installation basic and Advance.                
b. Teaming.                                                  
c. Dmaas.                                                           
d. OpenEBS upgrade.                                                                       
f. Control Plane upgrade. 
g. AD authentication(lowest priority)                                                   
   
### 8.0 Test execution cycle:
a. Test cases will be written for new fearures.                                                           
b. E2E team will get the APIs for new features 10 days in advance.                                                               
c .E2E team will automate the test cases written for new features using the APIs given by dev team. Until the code is merge these test  cases will fail in pipeline. This is the first time tests will be executed.                                           
d. Once dev team PR got merges the test cases will be validated in the pipeline. This is the second time tests will be executed.          e. Bases on the pipeline status dev and test team will verify either the code or test case implementation.                         

### 9.0 Correlation between testing cycles and release plan:
The release of DOP is 15th of every month.                                                               
Test execution will happen in two cycles:                                                 
 a. When E2E team ready will the automated test cases with the provided rest APIs from dev team.                                   
 b. When code of dev team merges to master branch.                                        
Before release all the test cases written for a feature(p0) should pass/fail based on the condition.                               
Set of test cases taken for GUI automation for a particular release should also pass/fail based on the condition.                        
### 10.0 Test budgets according to project or overall operational budget:                    
The amount decided to be spend on servers,cloud providers, internet etc.                                      

### 11.0 Interrelation between other departments and testing team:
a. There should be shared responsibility between devloper and tester to make the product much stable and successful.                     
b. If the pipeline fails then tester and developer should help each other to find the issue and fix the same.                           
c. The end goal should be only product quality.                                                 

### 12.0 Risks associated with test project
a. Delay in the test build to test/E2E team.                                 
b. Unavailability of test environment.                                      
c. Delay in fixing defects by development team.                                      
d. Major changes in the SRS(Software requirements specifications) which invalidates the current test cases and requires changes in the test case and its implementation.       

### 13.0 Management and control of testing
a. Priortizing the Test cases. P0 test cases should be must covered for every release.                                          
b. Priortizing the test effort. In case, if automating a test case is taking more than expected time then we should pick next test case and put the current test case in backlog.
c. If all the P0 test cases are covered then we can take P1 test cases.            

### 14.0 Roles and responsibilities

#### 14.1 Test lead is responsible for:
a. Defining the testing activities for subordinates – testers or test engineers.                                        
b. All responsibilities of test planning.                                                                    
c. To check if the team has all the necessary resources to execute the testing activities.                                       
d. To check if testing is going hand in hand with the software development in all phases.                                 
e. Prepare the status report of testing activities.                                                         
f. Required Interactions with customers.                                                                              
g. Updating project manager regularly about the progress of testing activities.   
h. Develop test cases and prioritize testing activities.                           

#### 14.2 Tester/E2E engineer are responsible for:
a. To read all the documents and understand what needs to be tested.                                                                     
b. Based on the information procured in the above step decide how it is to be tested.                  
c. Inform the test lead about what all resources will be required for software testing.                                   
d. Execute all the test case and report defects, define severity and priority for each defect.      
e. Carry out regression testing every time when changes are made to the code to fix defects.                   

### 15.0 Inputs and outputs for each test level:
TO DO

### Approvals:
Ajesh                                                                 
Uma                                                                  
Amit                                                                             































 





























