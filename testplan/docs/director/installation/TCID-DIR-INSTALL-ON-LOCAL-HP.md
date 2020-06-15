---
id: TCID-DIR-INSTALL-ON-LOCAL-HP
title: Install DOP using helm with SSD underneath
sidebar_label: TCID-DIR-INSTALL-ON-LOCAL-HP
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
    <td>TCID-DIR-INSTALL-ON-LOCAL-HP</td>
    <td>Deploying Director on-prem</td>
    <td> Install DOP using helm with SSD underneath </td>
  </tr>
</table>

### Prerequisites

- K8s should be installed in the cluster.
- Openebs should be installed on the cluster.

### Steps Performed in the test

- Clone director-charts-internal repository .
- Get into latest release directory of helm chart .
- Create secret having maya-init repo access .
`kubectl create secret docker-registry directoronprem-registry-secret --docker-server=registry.mayadata.io --docker-username=<docker-user>--docker-password=<docker-password>
`
- Create clusterrolebinding
`kubectl create clusterrolebinding kube-admin --clusterrole cluster-admin --serviceaccount=kube-system:default
`
- Replace storageClass to be used to openebs-hostpath in values.yaml
`sed 's/storageClass: standard/storageClass: openebs-hostpath/' -i values.yaml`
- Apply helm chart
`helm install --name dop . --set server.url=< dop_url > --set nginx-ingress.enabled=false`
- Wait for the DOP components up and running , Using sleep time 600ms 
- Enter on platform-repo ( OEP-E2E-RANCHER ) path 
 `cd ~/<platform-repo>`

<b>Install litmus pre-requisites</b>
- Clone oep-e2e repository which contains all the test scripts.
`git clone https://github.com/mayadata-io/oep-e2e.git`
- Setup litmus on the Cluster
`
kubectl apply -f oep-e2e/litmus/prerequisite/rbac.yaml
kubectl apply -f oep-e2e/litmus/prerequisite/crds.yaml
kubectl apply -f oep-e2e/litmus/prerequisite/docker-secret.yml
`
- Generate URL to access DOP 
- Create a configmap from DOP URL
`kubectl create configmap config --from-literal=url=<generated-DOP-URL> -n litmus`

<b>Running basic sanity checks</b> <br>

Using Basic-sanity-check script to check the DOP components , If any of the component fails job will fail .

### Expected Result 

- Every component of DOP cluster should be healthy and running.

### Test Result Link

- https://github.com/mayadata-io/oep-e2e-results/tree/master/TCID-DIR-INSTALL-ON-LOCAL-HP
