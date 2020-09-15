---
id: monitoring
title: Monitoring Manual Tests
sidebar_label: Monitoring
---

### Pre-requisites

- Kubera OnPrem Director predeployed (incase the testing is being done on on-premise version of Kubera). Kubera can be deployed using [Kubera charts](https://charts.mayadata.io/).
- A k8s cluster having disks attached to its nodes. These disks will be used to create cstor-pools and deploy applications that will use these volumes.

The following steps needs to be performed as a part of the manual tests for Monitoring -

- Connect the k8s cluster to Kubera Director or Kubera OnPrem Director. To know more visit [MayaData](https://portal.mayadata.io/).
- Deploy OpenEBS on the cluster connected to Kubera (using [Kubera](https://blog.mayadata.io/overview-set-up-configure-kubera) or [helm](https://openebs.github.io/charts/) or [operator yaml](https://github.com/openebs/openebs/blob/master/k8s/openebs-operator.yaml)).

### Deploying applications on different OpenEBS storage engines

#### OpenEBS Hostpath

Deploy busybox application using openebs-hostpath. Use the below yaml to deploy busybox -

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-hp
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: openebs-hostpath
  resources:
    requests:
      storage: 2Gi
---
apiVersion: v1
kind: Pod
metadata:
  name: busybox-hp
  namespace: default
spec:
  containers:
  - command:
       - sh
       - -c
       - 'date > /mnt/store1/date.txt; hostname >> /mnt/store1/hostname.txt; sync; sleep 5; sync; tail -f /dev/null;'
    image: busybox
    imagePullPolicy: Always
    name: busybox
    volumeMounts:
    - mountPath: /mnt/store1
      name: demo-vol1
  volumes:
  - name: demo-vol1
    persistentVolumeClaim:
      claimName: pvc-hp
---
```

#### OpenEBS Cstor

> Note: In case openEBS is deployed using Kubera use the below yaml for creating the storage class -

```
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: openebs-cstor-disk
  annotations:
    openebs.io/cas-type: cstor
provisioner: cstor.csi.openebs.io
allowVolumeExpansion: true
parameters:
  replicaCount: "3"
  cas-type: cstor
  cstorPoolCluster: <cspc-name>
```

Create a striped/mirrored cstorpool using the disks attached from Kubera and deploy percona using the cstor storage class. Use the below yaml for deploying percona -

```
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: percona
  labels:
    app: percona 
    openebs.io/target-affinity: percona
spec:
  replicas: 1
  selector: 
    matchLabels:
      app: percona 
  template: 
    metadata:
      labels: 
        app: percona
        openebs.io/target-affinity: percona
    spec:
      containers:
        - resources:
            limits:
              cpu: 0.5
          name: percona
          image: openebs/tests-custom-percona:latest
          imagePullPolicy: IfNotPresent
          args:
            - "--ignore-db-dir"
            - "lost+found"
          env:
            - name: MYSQL_ROOT_PASSWORD
              value: k8sDem0
          ports:
            - containerPort: 3306
              name: percona
          volumeMounts:
            - mountPath: /var/lib/mysql
              name: data-vol
          livenessProbe:
            exec:
              command: ["bash", "sql-test.sh"]
            initialDelaySeconds: 60
            periodSeconds: 1
            timeoutSeconds: 10 
      volumes:
        - name: data-vol
          persistentVolumeClaim:
            claimName: pvc-cstor 
---
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: pvc-cstor 
  labels: 
    openebs.io/target-affinity: percona  
spec:
  storageClassName: openebs-cstor-disk 
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 2Gi
---
apiVersion: v1
kind: Service
metadata:
  name: percona-mysql
  labels:
    app: percona 
spec:
  ports:
    - port: 3306
      targetPort: 3306
  selector:
      app: percona
```


Generating load on percona:

For generating load on percona, we’ll be using tpcc-client. [TPC-C](http://www.tpc.org/tpcc/) is an On-Line Transaction Processing Benchmark. For more details visit this [link](https://github.com/openebs/e2e-tests/tree/master/apps/percona/workload).

Create a configmap using - `kubectl create configmap tpcc-config --from-file tpcc.conf` and use the below tpcc.conf file -

```
{
  "db_user": "root",
  "db_password": "k8sDem0",
  "warehouses": "1",
  "connections": "18",
  "warmup_period": "10",
  "run_duration": "600",
  "interval": "10"
}
```

Apply the following loadgen job - `kubectl apply -f tpcc_bench.yml` using the below tpcc_bench.yml after replacing the IP in args with the IP of the percona service -

```
---
apiVersion: batch/v1
kind: Job
metadata:
  name: tpcc-bench
spec:
  template:
    metadata:
      name: tpcc-bench
      labels:
        loadgen: percona-loadgen
    spec:
      restartPolicy: Never
      containers:
      - name: tpcc-bench 
        image: openebs/tests-tpcc-client
        command: ["/bin/bash"]
        args: ["-c", "./tpcc-runner.sh 10.43.164.114 tpcc.conf; exit 0"]
        volumeMounts:
        - name: tpcc-configmap
          mountPath: /tpcc-mysql/tpcc.conf
          subPath: tpcc.conf
        tty: true 
      volumes:
        - name: tpcc-configmap
          configMap:
            name: tpcc-config
```

### Testing Kubera

Inside Kubera select the cluster that was connected. Go to the Volumes and Monitor section present in the sidebar of Kubera. Select each volume one after the other and see if everything is working fine or not in Monitoring.

### Examples

Monitor section of Kubera --

![alt text](https://github.com/mayadata-io/oep-e2e/blob/master/testplan/static/img/monitor.png 'Monitor')

Volume section of Kubera --

![alt text](https://github.com/mayadata-io/oep-e2e/blob/master/testplan/static/img/volumes.png 'Volumes')