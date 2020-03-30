---
id: install-tcid-iudi01
title: Install-GCP-TCID-IUDI01
sidebar_label: TCID-IUDI01
---
------


## Install DOP using helm on GCP with GPD underneath

### Experiment Metadata

<table>
  <tr>
    <th> Type </th>
    <th> Description </th>
    <th> Tested K8s Platform </th>
  </tr>
  <tr>
    <td> Install of DOP </td>
    <td> Install DOP using helm on GCP with GPD underneath </td>
    <td> GCP </td>
  </tr>
</table>

### Prerequisites

- Bring up 4 Vms in GCP 1 master 3 node.                                         
- Use any tool such as kops to spin up k8s cluster. It is suggested to have k8s version >= 1.12.0                         
- All the nodes of the cluster should be in healthy state.     
- helm 3 should be installed on the k8s cluster.


### Details
- In this test case we have to spin up a k8s cluster on top of GCP VMs and install DOP on the k8s cluster.       

### Steps Performed in the test

- Clone the director-charts-internal repo.

- Create a namespace on which DOP should be.

- Create a secret in the above namespace .

- Provide the secret and  URL in the values.yaml.

- Use storage class as standard for all the PVCs .

- Execute the helm install command. Follow the helpcenter doc for detailed information.                      


### Expected output

- All the DOP pods should come in running state.
- All the pods in maya-system namespace should be running state.
- DOP ui should be accessible in any browser.
