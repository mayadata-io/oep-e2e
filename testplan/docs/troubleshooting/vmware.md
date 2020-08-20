# ***K8s clusters on VMware***

Kubera E2E started off by using public cloud platforms such as AWS, GCP to execute E2E test scenarios. However, cloud expenses did bother us a lot leading to setting up on premise infrastructure to reduce this cost. Team started using VMware Vsphere to set up virtual machines for various Kubernetes distributions such as OpenShift, D2IQ Konvoy, and Rancher.

The page will discuss about this environment and the challenges faced so far to run E2E pipelines.

### **Setting up the cluster environment**

When we were using the public cloud platforms, we used to create the cluster at the beginning of every CI pipeline and delete it at the end. In the case of VMware environment, it takes much time for creating virtual machines and then to configure the Kubernetes cluster. Approximately, it takes almost an hour for configuring a new cluster. In order to overcome this, we leverage VMware snapshotting/restoring feature. After creating a Kubernetes cluster with the desired distribution, say, Rancher, OpenShift, D2IQ Konvoy, and Kubeadm based, a VMware snapshot was created for each virtual machine to hold the state of the machine. Once the pipeline is completed, all the VM instances are reverted back using this snapshot. So, all the configurations created as part of the pipeline would be deleted and resemble a freshly configured Kubernetes cluster.
At the beginning of the pipeline, we check if the cluster is healthy and if all the components are running successfully. And then, we execute various OpenEBS specific E2E Scenarios in various Gitlab stages. Finally, in the end, we revert back all the VM instances to the earlier state using snapshots.

For reference, please check [pipelines](https://oep-pipelines.mayadata.io/)

### **Challenges in using such an on-premise environment**

#### **Boot storm:**

After reverting the VM instances at the end of every pipeline, we are rebooting the instances to schedule the microservices components in Kubernetes again. We are rebooting to clear out the in-memory processes while capturing snapshots. When we restart all the VM instances at once, we hit a boot storm issue sometimes. Some of the virtual machines are failed to restart due to this. In order to mitigate this issue, we tend to induce a very minimal sleep in between rebooting the different instances rather than doing it at once.

#### **Resource outages:**

This is one of the most common challenges which we face when we add more jobs to the pipeline. But it is not a difficult task to upgrade the resources of virtual machines if the corresponding ESX has enough unused resources. 

#### **Thin Provisioning:**

We leverage the Thin provisioning feature of VMware for doing over-provisioning of storage resources to the virtual machine instances. When the resource utilization reaches the threshold, the machines were observed to be stuck. As an effect, it is recommended to plan and provision the resources based on the availability of resources in the hypervisor.

#### **Virtual machine memory snapshots:**

In our use case, the virtual machine’s memory is not required in snapshots. While creating the virtual machine snapshot, by default, it is enabled. Sometimes, such in-memory processes are not cleared out in our microservices environment though we reboot the instances after reverting the virtual machines due to boot storm which was pointed out above. It is recommended to disable this option while creating virtual machine snapshots.

#### **Virtual Disk Errors:**

Sometimes, the virtual machines are stuck at the boot prompt with disk errors when we reboot them. It is an error that occurs due to file system error on Ubuntu. It doesn’t proceed further without human intervention.

![img](https://lh4.googleusercontent.com/2J35ko05O6nltgzeo9dcmBg_sZtRj7Jb-XF-aUssMQwGl5xKVhkgQGE9cYPyw5FE_xZvn7W3-WwAQ09WjVs52o_zAYsXh_3flWu11da9g0ZaEwRFHe0qDxinPstFixcCWnhsIoS5)

We need to clear the errors on specified disk by executing the command `e2fsck -y /dev/<disk name>`. This will check the file system consistency and clear the errors which enable the virtual machine to proceed further.