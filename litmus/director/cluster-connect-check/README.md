# Creating a k8s cluster on GCP

The following steps are performed for creating a kubernetes cluster on GCP:

- Authorise using SDK token.
- Set google cloud project.
- Clone the mayadata-io litmus repository -- https://github.com/mayadata-io/litmus
- Get into the following directory `litmus/k8s/gcp/k8s-installer/`
- Create VPC using the playbook  `create-vpc.yml` and pass the project in which the cluster is to be created as an env variable.
- Create the cluster using the playbook `create-k8s-cluster.yml` and pass the project, number of nodes and k8s version as env variables.
- Check cluster availability using the following playbook `check-cluster-availability.yml` and pass the no of nodes as an env variable.
- Apply the following litmus rbac yaml from openebs litmus repository -- https://raw.githubusercontent.com/openebs/litmus/master/hack/rbac.yaml
- Create a firewall rule to allow tcp traffic on port 30380.