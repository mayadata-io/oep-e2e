# configs-db check

The following checks are performed on configs-db:

- Initial common checks:
    - Check the memory consumption of the nodes. If the memory consumption is greater than 90 percent the check fails.
    - Check the CPU consumption of the nodes. If the CPU consumption is greater than 90 percent the check fails.
    - Check if the configs-db pod exists and is running or not. If the pod is not running the check fails.

- App specific checks:
    - Check if configs db exists. Fails if configs db is not found