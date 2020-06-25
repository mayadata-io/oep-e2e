---
id: TCID-DIR-DMAAS-SCHD-LOCAL-DEV-MINIO-BUCKET
title: Restore Minio application
sidebar_label: TCID-DIR-DMAAS-SCHD-LOCAL-DEV-MINIO-BUCKET
---
------

### Experiment Metadata

<table>
  <tr>
    <th> TCID </th>
    <th> Type </th>
    <th> Description </th>
  </tr>
  <tr>
    <td> TCID-DIR-DMAAS-SCHD-LOCAL-DEV-MINIO-BUCKET </td>
    <td> Dmaas Backup and Restore </td>
    <td> Verify dmaas restore minio application deployed using local-device and Minio bucket used to restore backup </td>
  </tr>
</table>

### Prerequisites
- DOP should be installed
- Minio application should be deployed on source cluster.

### Details
- Director version 1.9 onwards
- Positive test case

### Steps Performed in the test

- Access the DOP url.
- Login using credentials.
- Click on Cluster tab.
- Click on Source cluster.
- Click on Application tab.
- Search minio application.
- Click on minio application having namespace is device-minio.
- Click on dmaas.
- Click on the New schedule button.
- Select Minio cloud provider.
- Click on Add cloud credentail button.
- Enter  minio username and password and save it.
- Enter minio server url where backup will be stored.
- Select schedule time interval.
- Click on Schedule now button to schedule backup.
- Click on created schedule.
- click on Restore icon.
- Select the destination cluster name from dropdown.
- Click on Restore button to start restore.
- Click on check status of Restore link.
- Click on Dmaas tab on Side panel.
- Serach for Dmaas schedule and click on schedule.
- Verify the status of dmaas restore. 

### Expected output

- Restore status should be Success and application should get restored to the destination cluster.

### Test Result Link

- https://github.com/mayadata-io/oep-e2e-results/tree/master/TCID-DIR-DMAAS-SCHD-LOCAL-DEV-MINIO-BUCKET
