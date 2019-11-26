## maya-io-server-check job design

- Checking cpu and memory consumption of all cluster's nodes
  - Failed_when: 
    - cpu or memory consumption percentage is more than threshold
  - Note: Threshold = 90%

- Check if application pod exists and is running

- Check if server is alive
  - Fetch director ip and check ping/pong connection
