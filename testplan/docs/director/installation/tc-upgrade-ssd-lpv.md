---
id: tc-upgrade-ssd-lpv
title: DOP Upgrade 
sidebar_label: TC-Upgrade-SSD-Lpv
---
------


### Upgrade DOP using helm with SSD underneath

### Experiment Metadata

<table>
  <tr>
    <th> TCID </th>
    <th> TC NAME </th>
    <th> Type </th>
    <th> Description </th>
  </tr>
  <tr>
    <td> TCID-iudu02 </td>
    <td> TC-Upgrade-SSD-Lpv </td>
    <td> Upgrade of DOP </td>
    <td> Upgrade DOP using helm with SSD underneath </td>
  </tr>
</table>


### Prerequisites

- All the nodes of the cluster should be in healthy state.
- All the pods of director should be in healthy/running state.                         
- helm 3 should be installed on the k8s cluster.


### Details
- In this test case we will upgrade DOP from older version to new version (eg:1.7.0 to 1.8.0) which is installed using sc as openebs-hostpath.       

### Steps Performed in the test

- Clone the director-charts-internal repo.

- Change the directory to new version of DOP(eg: 1.8.0)

- Copy the secret from values.yaml of older version of DOP(eg:1.7.0) to new version of DOP(eg:1.8.0)

- Copy the URL from values.yaml of older version of DOP(eg:1.7.0) to new version of DOP(eg:1.8.0)

- Use storage class as openebs-hostpath for all the PVCs in new version of DOP values.yaml.

- Execute the **helm ls** command to get the release name.

- Execute the helm upgrade command to upgrade the DOP. Follow the helpcenter doc for detailed information <a href="https://help.mayadata.io/hc/en-us/articles/360033029812-Upgrading-Director-OnPrem" target="_blank">helpcenter</a> .                     


### Expected output

- helm ls command should show the new version of DOP.
- DOP ui should be accessible in any browser.
