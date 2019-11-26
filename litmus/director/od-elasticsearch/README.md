# od-elasticsearch checks

The following checks are performed on od-elasticsearch:

- Initial common checks:
    - Check the memory consumption of the nodes. If the memory consumption is greater than 90 percent the check fails.
    - Check the CPU consumption of the nodes. If the CPU consumption is greater than 90 percent the check fails.
    - Check if the od-elasticsearch pod is running or not. If the pod is not running the check fails.

- App specific checks:
    - Check if the elasticsearch shards are in healthy state or not. If the status of elasticsearch shards is red the check fails.