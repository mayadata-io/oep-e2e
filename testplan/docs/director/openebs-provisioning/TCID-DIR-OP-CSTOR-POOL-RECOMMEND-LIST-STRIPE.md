---
id: TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-STRIPE
title: List stripe based cstor pool recommendations
sidebar_label: TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-STRIPE
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
    <td> TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-STRIPE </td>
    <td> CStorPool Recommendation </td>
    <td> Verify List of Stripe Recommendations </td>
  </tr>
</table>

### Prerequisites
- Cluster create setup should be done
- DOP should be installed
- BlockDevices should be detected by NDM

### Details
- Director version 1.9 onwards
- Positive test case

### Steps Performed in the test

- Invoke API to list recommendations
- Invoke API to get capacity based recommendations
- Invoke API to get device based recommendations
- Invoke API to get stripe based cstor pool recommendations

### Expected output

- Director should list stripe based cstor pool recommendations

### Test Result Link

- https://github.com/mayadata-io/oep-e2e-results/tree/master/TCID-DIR-OP-CSTOR-POOL-RECOMMEND-LIST-STRIPE