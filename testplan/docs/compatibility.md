---
id: compatibility
title: Kubera Test Compatibility Matrix
sidebar_label: Compatibility Matrix
---

This page captures platforms and components used while testing each version of Kubera Version. It can be used to derive the platform compatibility chart. 

## Kubera Version 1.9

**Platforms and Details listed below**

###  Rancher

**Cluster1**

- Rancher version - v2.3.5 
- k8s version - v1.15.9
- OS - CentOS Linux 7
- Docker version - 1.13.1
- Weave version - 2.5.2
- Tiller version - v2.14.3
- Etcd version - coreos-etcd:v3.3.10-rancher1

**Cluster2**

- Rancher version - v2.3.5
- k8s version - v1.15.11
- OS - CentOS Linux 7
- Docker version - 1.13.1
- Weave version - 2.5.2
- Tiller version - v2.14.3
- Etcd version - coreos-etcd:v3.3.10-rancher1

###  Konvoy

**Cluster C1**

- Konvoy version: v1.2.4
- OS version: centos-release-7-7.1908.0.el7.centos.x86_64
- Kubernetes version: v1.15.5
- Kernel version: 3.10.0-1062.el7.x86_64   
- Containerd version: containerd://1.2.6
- Calico version: v3.8.2
- Tiller version: v2.16.6
- CoreDNS version: 1.3.1
- etcd version: 3.3.10
- Keepalived Image: mesosphere/keepalived-snmp:v0.1
- Kubectl Version: v1.15.0  

**Cluster C2**

- Konvoy version: v1.4.1
- OS version: centos-release-7-7.1908.0.el7.centos.x86_64
- Kubernetes version: 1.16.4
- Kernel version: 3.10.0-1062.el7.x86_64   
- Containerd version: containerd://1.2.6
- Calico version: v3.10.1
- Tiller version: v2.16.1
- CoreDNS version: 1.6.2
- etcd version: 3.3.15-0
- Keepalived Image: mesosphere/keepalived-snmp:v0.1
- Kubectl Version: v1.15.0

**Cluster C3**

- Konvoy version: v1.2.4
- OS version: centos-release-7-7.1908.0.el7.centos.x86_64
- Kubernetes version: 1.15.5
- Kernel version: 3.10.0-1062.el7.x86_64   
- Containerd version: containerd://1.2.6
- Calico version: v3.8.2
- Tiller version: v2.14.3
- CoreDNS version: 1.3.1
- etcd version: 3.3.10-0
- Keepalived Image: mesosphere/keepalived-snmp:v0.1
- Kubectl Version: v1.15.0


###  AWS

**Cluster1 and Cluster2**

- OS version - Ubuntu Server 18.04 LTS (HVM), SSD Volume Type
- K8S Version - 1.17.6
- KOPS version - Version 1.16.0
- kuberouter - v0.3.1
- tiller - v2.14.3
- etcd - 3.3.10




