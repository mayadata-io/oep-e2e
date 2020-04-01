---
id: tc-install-gcp-jiva
title: DOP Install on GCP with Jiva
sidebar_label: TC-Install-GCP-Jiva
---
------


### Install DOP using Jiva storage class with SSD disks underneath.

### Experiment Metadata

<table>
  <tr>
    <th> TCID </th>
    <th> TC NAME </th>
    <th> Type </th>
    <th> Description </th>
  </tr>
  <tr>
    <td> TCID-iudi05 </td>
    <td> TC-Install-GCP-Jiva </td>
    <td> Install of DOP </td>
    <td> Install DOP using helm on GCP and sc as openebs-jiva-default </td>
  </tr>
</table>

### Prerequisites

- Bring up 4 Vms in GCP 1 master 3 node.Select SSD disk during bringing up Vms.            
- Use any tool such as kops to spin up k8s cluster. It is suggested to have k8s version >= 1.12.0                         
- All the nodes of the cluster should be in healthy state.     
- helm 3 should be installed on the k8s cluster.


### Details
- In this test case we will install DOP on the k8s cluster using storage class as openebs-jiva-default. 

### Steps Performed in the test

- Install OpenEBS latest version from OpenEBS doc. Use helm or operator method for it.

- Clone the director-charts-internal repo.

- Create a namespace on which DOP should be.

- Create a secret in the above namespace .

- Provide the secret and  URL in the values.yaml.

- Use storage class as openebs-jiva-default for all the PVCs .

- Execute the helm install command. Follow the helpcenter doc for detailed information.                      


### Expected output

- All the pods in openebs namespace should be in running state. List of pods:
```
maya-apiserver-77b49c99f5-vdckq                                   
openebs-admission-server-77d489c57d-pxpm5                         
openebs-localpv-provisioner-8447b496c7-jc927                      
openebs-ndm-2fkfq                                                 
openebs-ndm-k4tsh                                                 
openebs-ndm-operator-f64c5bb7-qczqf                               
openebs-ndm-sgrn7                                                 
openebs-provisioner-557d489db8-kprrm                              
openebs-snapshot-operator-6d48b74fdb-47qqp
```

- All the DOP pods should come in running state. List of pods:
```
alertmanager-874ddc6dd-fv7fg
alertstore-6669f5c5fc-jrgm6
alertstore-tablemanager-5d966c867f-l5xth
cassandra-0
chat-server-57bfb8545c-w2hj9
cloud-agent-6d4ddc686c-jwgd6
configs-57f4b5c7c6-n722c
configs-db-74d4fcd6c9-zlb5r
consul-6c775c669-zzkck
distributor-75bd5d646-n6gc2
elastalert-5d59db79b-24hvt
ingester-7976f847d4-dl9vt
maya-grafana-848946789f-kqh64
maya-io-7bfb4d988b-nfl4h
maya-ui-8484df85d7-hb844
memcached-f76c997dd-tkkhl
mysql-0
od-elasticsearch-logging-0
od-kibana-logging-66bb8c7b7c-qz4sj
querier-54765f4b8c-ts7hw
ruler-645f94f6bc-vswbp
table-manager-bcd58f7df-wvrkr
```
- All the pods in maya-system namespace should be running state.
- DOP ui should be accessible in any browser.
