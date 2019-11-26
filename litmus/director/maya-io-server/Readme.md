## maya-io-server-check job design

- Checking cpu and memory consumption of all cluster's nodes
  Failed_when: 
  - cpu or memory consumption percentage is more than threshold
  Threshold: 90%

- Check if application pod exists and is Running

- Check if server is Alive
  - Fetch director ip and check ping/pong connection