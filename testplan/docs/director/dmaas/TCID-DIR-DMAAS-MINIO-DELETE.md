---
id: TCID-DIR-DMAAS-MINIO-DELETE
title: Delete schedules created using Minio bucket
sidebar_label: TCID-DIR-DMAAS-MINIO-DELETE
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
    <td> TCID-DIR-DMAAS-MINIO-DELETE </td>
    <td> Dmaas schedule deletion </td>
    <td> Verify dmaas schedules deletion created using Minio bucket</td>
  </tr>
</table>

### Prerequisites
- DOP should be installed
- Minio application should be deployed on source cluster and schedules to be present for application using Minio bucket.

### Details
- Director version 1.9 onwards
- Positive test case

### Steps Performed in the test

- Access the DOP url.
- Login using credentials.
- Open Dmaas page.
- Delete schedules using Minio bucket. 

### Expected output

- Dmaas schedule should be removed which are using minio bucket.

### Test Result Link

- https://github.com/mayadata-io/oep-e2e-results/tree/master/TCID-DIR-DMAAS-MINIO-DELETE
