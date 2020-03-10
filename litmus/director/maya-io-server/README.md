# maya-io-server check

The following checks are performed on maya-io-server:

- Initial common checks:
    - Check the memory consumption of the nodes. If the memory consumption is greater than 90 percent the check fails.
    - Check the CPU consumption of the nodes. If the CPU consumption is greater than 90 percent the check fails.
    - Check if the maya-io-server pod exists and is running or not. If the pod is not running the check fails.

- App specific checks:
    - Check if server is alive using ping/pong connection (“ping/pong frames” are used to check the connection, sent from the server, the browser responds to these automatically). Requesting director-ip:port/ping and if response is not pong then check fails