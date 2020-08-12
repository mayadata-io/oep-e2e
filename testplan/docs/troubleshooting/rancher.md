---
id: rancher
title: Rancher Troubleshooting
sidebar_label: Rancher
---

## Issues

### Issue1: Openebs installation failing on cluster2

#### What is the issue?

In the Rancher pipeline, the installation of OpenEBS via Kubera OnPrem Director was stuck. On investigating more we found out that openebs-upgrade and cstorpoolauto pod present in maya-system namespace was showing the following error -

```
E0730 05:58:27.664789       1 discovery.go:184] API resource discovery failed: unable to retrieve the complete list of server APIs: metrics.k8s.io/v1beta1: the server is currently unable to handle the request
```

On running kubectl get apiservices we got the below output -

```
NAME                                   SERVICE                      AVAILABLE                      AGE
v1beta1.extensions                     Local                        True                           103d
v1beta1.metrics.k8s.io                 kube-system/metrics-server   False (FailedDiscoveryCheck)   103d
v1beta1.networking.k8s.io              Local                        True                           103d
v1beta1.node.k8s.io                    Local                        True                           103d
```

On describing v1beta1.metrics.k8s.io we found out that it was showing the below message -

```
failing or missing response from https://10.43.124.28:443/apis/metrics.k8s.io/v1beta1: Get https://10.43.124.28:443/apis/metrics.k8s.io/v1beta1: dial tcp 10.43.124.28:443: connect: no route to host
```

On getting services present in all namespaces we found that 10.43.124.28 is the service of metrics-server and the logs of the metrics-server was showing the below error continuously -

```
E0729 19:29:05.246553       1 manager.go:111] unable to fully collect metrics: [unable to fully scrape metrics from source kubelet_summary:oep-rancher-node2: [unable to get CPU for node "10.53.1.12", discarding data: missing cpu usage metric, unable to get CPU for container "weave-plugins" in pod kube-system/weave-net-nbrz7 on node "10.53.1.12", discarding data: missing cpu usage metric, unable to get CPU for container "weave" in pod kube-system/weave-net-nbrz7 on node "10.53.1.12", discarding data: missing cpu usage metric, unable to get CPU for container "weave-npc" in pod kube-system/weave-net-nbrz7 on node "10.53.1.12", discarding data: missing cpu usage metric, unable to get CPU for container "nginx-ingress-controller" in pod ingress-nginx/nginx-ingress-controller-2xzvq on node "10.53.1.12", discarding data: missing cpu usage metric, unable to get CPU for container "agent" in pod cattle-system/cattle-node-agent-kgb2q on node "10.53.1.12", discarding data: missing cpu usage metric, unable to get CPU for container "autoscaler" in pod kube-system/coredns-autoscaler-65bfc8d47d-4zj2n on node "10.53.1.12", discarding data: missing cpu usage metric], unable to fully scrape metrics from source kubelet_summary:oep-rancher-node1: unable to fetch metrics from Kubelet oep-rancher-node1 (10.53.1.11): Get https://10.53.1.11:10250/stats/summary?only_cpu_and_memory=true: dial tcp 10.53.1.11:10250: connect: connection refused]
```

#### How did we fix it?

Restarting the metrics-server pod fixed the issue. So we restarted the metrics-server pod and took a snapshot of the VM’s of the cluster.