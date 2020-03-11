# consul check

The following checks are performed on consul:

- Initial common checks:
    - Check the memory consumption of the nodes. If the memory consumption is greater than 90 percent the check fails.
    - Check the CPU consumption of the nodes. If the CPU consumption is greater than 90 percent the check fails.
    - Check if the consul pod exists and is running or not. If the pod is not running the check fails.

- App specific checks:
    - Check if consul node status is 'alive' using command "consul members" (The members command outputs the current list of members that a Consul agent knows about, along with their state. The state of a node can only be "alive", "left", or "failed".)
    In the test this state of a node is fetched  and the test fails if state is not "alive"