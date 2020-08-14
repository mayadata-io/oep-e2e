---
id: rancher
title: Rancher Troubleshooting
sidebar_label: Rancher
---

## Issues

### Issue1: Openebs installation failing on cluster2

#### What is the issue?

In the Rancher pipeline, the installation of OpenEBS via Kubera OnPrem Director was stuck. On investigating more we found out that openebs-upgrade and cstorpoolauto pod present in maya-system namespace was showing the following error -

`
E0730 05:58:27.664789       1 discovery.go:184] API resource discovery failed: unable to retrieve the complete list of server APIs: metrics.k8s.io/v1beta1: the server is currently unable to handle the request
`

On running kubectl get apiservices we got the below output -

```
NAME                                   SERVICE                      AVAILABLE                      AGE
v1beta1.extensions                     Local                        True                           103d
v1beta1.metrics.k8s.io                 kube-system/metrics-server   False (FailedDiscoveryCheck)   103d
v1beta1.networking.k8s.io              Local                        True                           103d
v1beta1.node.k8s.io                    Local                        True                           103d
```

On describing v1beta1.metrics.k8s.io we found out that it was showing the below message -

`
failing or missing response from https://10.43.124.28:443/apis/metrics.k8s.io/v1beta1: Get https://10.43.124.28:443/apis/metrics.k8s.io/v1beta1: dial tcp 10.43.124.28:443: connect: no route to host
`

On getting services present in all namespaces we found that 10.43.124.28 is the service of metrics-server and the logs of the metrics-server was showing the below error continuously -

`
E0730 00:09:50.263424       1 manager.go:111] unable to fully collect metrics: [unable to fully scrape metrics from source kubelet_summary:oep-rancher-node2: unable to get CPU for container "busybox" in pod openebs/busybox1 on node "10.53.1.12", discarding data: missing cpu usage metric, unable to fully scrape metrics from source kubelet_summary:oep-rancher-node5: unable to get a valid timestamp for metric point for container "fluentd-forwarder" in pod maya-system/fluentd-forwarder-mc7jh on node "10.53.1.15", discarding data: no non-zero timestamp on either CPU or memory]
`

The above log suggested that there were some time mismatch between the nodes of the cluster.

#### How did we fix it?

To fix the timing mismatch issue, we set the correct time on each of the nodes. Restarting the metrics-server pod post setting the time resolved this issue. After restarting the pod we took a snapshot of the VM’s of the cluster.

#### Issue link

- https://github.com/mayadata-io/oep/issues/220