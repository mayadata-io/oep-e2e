---
id: kubera-dashboard
title: Kubera Manual Testing Dashboard
sidebar_label: Kubera dashboard
---

### Below test cases are executed manully for different type of dashboards 


#### To verify graphs are shown in Home dashboards 
- Graphs are shown for the openEBS volumes 

#### To verify active clusters and other clusters lists are shown in Home dashboard 
- Active clusters will show the list all the active clusters
- Other clusters will shows the list of inactive or offline clusters 

#### To verify in Home dashboards project team members are shown 
- Project team members are shown with respective roles 

#### To verify alerts are shown and clickable for Active clusters in Home dashboard
- Alert should be shown in UI 
- Clicking on alerts should redirect to Alert dashboard 

#### To verify the cluster search functionality  
- The respective cluster should be shown in UI 

#### Cluster dashboard should show the status of all the cluster connected to Kubera OnPrem 
- Active,inactive and offline clusters should be shown  

#### To verify the k8s version for different active and offline clusters 
- Clusters version should be shown for both active and offline clusters
- Cluster version should not be shown for inactive clusters 

#### To verify that disconnect text should be present for delete icon and the pop up message should also have disconnect text
- Disconnect should be shown
- After clicking on disconnect icon disconnect pop message should be shown

#### To verify volume monitoring graphs are shown in cross cloud monitoring dashboard
- Monitoring graphs are shown

#### To acknowledge single alert in Alerts dashboard
- Single alert should get acknowledged

#### To acknowledge bulk alerts in Alert dashboard
- All the selected alerts should get acknowledged

#### Dmaas dashboard should show list of schedules and list of restores
- Shows list of backups and restores

#### To verify User and Roles dashboard view
- All users can be view.
- Pending invite for users can be viewed

#### To verify Overview dashboard
- Volume analytics graphs should be shown
- Kubera component status cann be viewed
- volume and pools which need attention can be viewed

#### To verify Application dashboard
- List of applications in the cluster will be seen

#### To verify Pools dashboard
- List of pools will be shown

#### To verify volume dashboard
- List of volumes will be shown with details

#### To verify Monitor dashboard
- List of volumes will be shown.
- Metric summary of all OpenEBS volumes are shown

#### To verify Logs dashboard
- Logs of OpenEBS components are shown 

#### To verify Alerts dashboard
- Cluster level alerts should be shown

#### To verify OpenEBS dashboard
- Contol plane component can be viewed
- Pool component can be viewed
- volumes can be viewed (execpt hostpath volumes)

#### To verify the storage pool dashboard
- Create cstor pool button is shown.
- All the pools are shown.

#### To verify the Nodes dashboard
- All the nodes should be shown along with RAM and CPU

#### To verify the Block Device dashboard
- All the bd in the cluster should be shown.
