# ingress-nginx check

The following checks are performed on ingress-nginx:

- Namespace specific checks:
    - Check if ingress-nginx namespace exists. Fails if namespace doesn't exist.
    - Check state of all pods running in ingress-nginx namespace. Fails if a pod is not in Running state.
    - Check readiness of all the pods in ingress-nginx namespace.
    - Check replicasets ready state inside the ingress-nginx namespace.