---
id: compatibility
title: OEP Test Compatbility Matrix
sidebar_label: Compatibility Matrix
---

This page captures platforms and components used while testing each version of OEP Version. It can be used to derive the platform compatibility chart. 

**OEP Version 1.9**

| OEP     | Cluster1                                                     |
| ------- | ------------------------------------------------------------ |
| Rancher | Cluster C1<br/>Rancher version - v2.3.5<br/>k8s version - v1.15.9<br/>OS - CentOS Linux 7<br/>Docker version - 1.13.1<br/>--------------------------------------------------------------------------------<br/>Cluster C2<br/>Rancher version - v2.3.5<br/>k8s version - v1.15.11<br/>OS - CentOS Linux 7<br/>Docker version - 1.13.1 |
| Konvoy  | Cluster C1<br/>Konvoy version: v1.2.4<br/>OS version: centos-release-7-7.1908.0.el7.centos.x86_64<br/>Kubernetes version: v1.15.5<br/>Kernel version: 3.10.0-1062.el7.x86_64   <br/>Containerd version: containerd://1.2.6<br/>Calico version: v3.8.2<br/>Tiller version: v2.16.6<br/>CoreDNS version: 1.3.1<br/>etcd version: 3.3.10<br/>Keepalived Image: mesosphere/keepalived-snmp:v0.1<br/>Kubectl Version: v1.15.0  <br/>--------------------------------------------------------------------------------<br/>Cluster C2<br/>Konvoy version: v1.4.1<br/>OS version: centos-release-7-7.1908.0.el7.centos.x86_64<br/>Kubernetes version: 1.16.4<br/>Kernel version: 3.10.0-1062.el7.x86_64   <br/>Containerd version: containerd://1.2.6<br/>Calico version: v3.10.1<br/>Tiller version: v2.16.1<br/>CoreDNS version: 1.6.2<br/>etcd version: 3.3.15-0<br/>Keepalived Image: mesosphere/keepalived-snmp:v0.1<br/>Kubectl Version: v1.15.0 |
| AWS     | OS version - Ubuntu Server 18.04 LTS (HVM), SSD Volume Type<br/>K8S Version - 1.15.10<br/>KOPS version - Version 1.16.0<br/>kuberouter - v0.3.1<br/>tiller - v2.14.3<br/>etcd - 3.3.10 |


