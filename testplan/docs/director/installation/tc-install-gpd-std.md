---
id: tc-install-gpd-std
title: DOP Install on GCP 
sidebar_label: TC-Install-GPD-Std
---
------


### Install DOP using helm with GPD underneath

### Experiment Metadata

<table>
  <tr>
    <th> TCID </th>
    <th> TC NAME </th>
    <th> Type </th>
    <th> Description </th>
  </tr>
  <tr>
    <td> TCID-iudi01 </td>
    <td> TC-Install-GPD-Std </td>
    <td> Install of DOP </td>
    <td> Install DOP using helm with GPD underneath </td>
  </tr>
</table>


### Prerequisites

- Bring up 4 Vms 1 master 3 node.                                         
- Use any tool such as kops to spin up k8s cluster. It is suggested to have k8s version >= 1.12.0                         
- All the nodes of the cluster should be in healthy state.     
- helm 3 should be installed on the k8s cluster.


### Details
- In this test case we will install DOP on the k8s cluster using storage class as standard.       

### Steps Performed in the test

- Clone the director-charts-internal repo.

- Create a namespace on which DOP should be.

- Create a secret in the above namespace .

- Provide the secret and  URL in the values.yaml.

- Use storage class as standard for all the PVCs .

- Execute the helm install command. Follow the helpcenter doc for detailed information.                      


### Expected output

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

### Test Results

<a href="https://github.com/mayadata-io/oep-e2e-results/tree/master/tcid-iudi01" target="_blank">View Test Results</a>