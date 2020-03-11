# mysql check

The following checks are performed on mysql:

- Initial common checks:
    - Check the memory consumption of the nodes. If the memory consumption is greater than 90 percent the check fails.
    - Check the CPU consumption of the nodes. If the CPU consumption is greater than 90 percent the check fails.
    - Check if the mysql pod exists and is running or not. If the pod is not running the check fails.

- App specific checks:
    - Check if maya db exists. Fails if maya db is not found
    - Check if mysql server is active by running 'mysqladmin  ping' command. Fails if command fails to run