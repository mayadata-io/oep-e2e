#!/bin/bash

## Run Prerequisites
echo -e "\n Running Prerequisites  *********************************************************************\n";
ls
echo -e "\n********* [ Making logs directory ] **********\n";
mkdir -p logs/director-health-checks -v

## Run OEP basic sanity checks
echo -e "\n Running OEP Basic Sanity Checks ************************************************************\n";

echo -e "------------------------------------------\n" >> result.txt
pwd
# Run maya-io-server check
echo -e "\n********** [ Running maya-io-server check ] **********\n";
chmod 755 ./oep/director-health-checks/maya-io-server-check.sh
./oep/director-health-checks/maya-io-server-check.sh > ./logs/director-health-checks/maya-io-server-check.log &

# Run maya-ui check
echo -e "\n************* [ Running maya-ui check ] **************\n";
chmod 755 ./oep/director-health-checks/maya-ui-check.sh
./oep/director-health-checks/maya-ui-check.sh > ./logs/director-health-checks/maya-ui-check.log &

# Run od-elasticsearch check
echo -e "\n********* [ Running od-elasticsearch check ] *********\n";
chmod 755 ./oep/director-health-checks/od-elasticsearch-check.sh
./oep/director-health-checks/od-elasticsearch-check.sh > ./logs/director-health-checks/od-elasticsearch-check.log &

# Run od-kibana check
echo -e "\n************ [ Running od-kibana check ] *************\n";
chmod 755 ./oep/director-health-checks/od-kibana-check.sh
./oep/director-health-checks/od-kibana-check.sh > ./logs/director-health-checks/od-kibana-check.log &

# Run alertmanager check
echo -e "\n*********** [ Running alertmanager check ] ***********\n";
chmod 755 ./oep/director-health-checks/alertmanager-check.sh
./oep/director-health-checks/alertmanager-check.sh > ./logs/director-health-checks/alertmanager-check.log &

# Run alertstore check
echo -e "\n************ [ Running alertstore check ] ************\n";
chmod 755 ./oep/director-health-checks/alertstore-check.sh
./oep/director-health-checks/alertstore-check.sh > ./logs/director-health-checks/alertstore-check.log &

# Run alertstore-tablemanager check
echo -e "\n****** [ Running alertstore-tablemanager check ] *****\n";
chmod 755 ./oep/director-health-checks/alertstore-tablemanager-check.sh
./oep/director-health-checks/alertstore-tablemanager-check.sh > ./logs/director-health-checks/alertstore-tablemanager-check.log &

# Run cassandra check
echo -e "\n************ [ Running cassandra check ] *************\n";
chmod 755 ./oep/director-health-checks/cassandra-check.sh
./oep/director-health-checks/cassandra-check.sh > ./logs/director-health-checks/cassandra-check.log &

# Run chat-server check
echo -e "\n*********** [ Running chat-server check ] ************\n";
chmod 755 ./oep/director-health-checks/chat-server-check.sh
./oep/director-health-checks/chat-server-check.sh > ./logs/director-health-checks/chat-server-check.log &

# Run cloud-agent check
echo -e "\n*********** [ Running cloud-agent check ] ************\n";
chmod 755 ./oep/director-health-checks/cloud-agent-check.sh
./oep/director-health-checks/cloud-agent-check.sh > ./logs/director-health-checks/cloud-agent-check.log &

# Run configs check
echo -e "\n************* [ Running configs check ] **************\n";
chmod 755 ./oep/director-health-checks/configs-check.sh
./oep/director-health-checks/configs-check.sh > ./logs/director-health-checks/configs-check.log &

# Run configs-db check
echo -e "\n************ [ Running configs-db check ] ************\n";
chmod 755 ./oep/director-health-checks/configs-db-check.sh
./oep/director-health-checks/configs-db-check.sh > ./logs/director-health-checks/configs-db-check.log &

# Run consul check
echo -e "\n************** [ Running consul check ] **************\n";
chmod 755 ./oep/director-health-checks/consul-check.sh
./oep/director-health-checks/consul-check.sh > ./logs/director-health-checks/consul-check.log &

# Run distributor check
echo -e "\n************ [ Running distributor check ] ***********\n";
chmod 755 ./oep/director-health-checks/distributor-check.sh
./oep/director-health-checks/distributor-check.sh > ./logs/director-health-checks/distributor-check.log &

# Run ingester check
echo -e "\n************* [ Running ingester check ] *************\n";
chmod 755 ./oep/director-health-checks/ingester-check.sh
./oep/director-health-checks/ingester-check.sh > ./logs/director-health-checks/ingester-check.log &

# Run ingress-nginx check
echo -e "\n********** [ Running ingress-nginx check ] ***********\n";
chmod 755 ./oep/director-health-checks/ingress-nginx-check.sh
./oep/director-health-checks/ingress-nginx-check.sh > ./logs/director-health-checks/ingress-nginx-check.log &

# Run maya-grafana check
echo -e "\n********** [ Running maya-grafana check ] ************\n";
chmod 755 ./oep/director-health-checks/maya-grafana-check.sh
./oep/director-health-checks/maya-grafana-check.sh > ./logs/director-health-checks/maya-grafana-check.log &

# Run memcached check
echo -e "\n************ [ Running memcached check ] *************\n";
chmod 755 ./oep/director-health-checks/memcached-check.sh
./oep/director-health-checks/memcached-check.sh > ./logs/director-health-checks/memcached-check.log &

# Run mysql check
echo -e "\n************** [ Running mysql check ] ***************\n";
chmod 755 ./oep/director-health-checks/mysql-check.sh
./oep/director-health-checks/mysql-check.sh > ./logs/director-health-checks/mysql-check.log &

# Run querier check
echo -e "\n************* [ Running querier check ] **************\n";
chmod 755 ./oep/director-health-checks/querier-check.sh
./oep/director-health-checks/querier-check.sh > ./logs/director-health-checks/querier-check.log &

# Run ruler check
echo -e "\n************** [ Running ruler check ] ***************\n";
chmod 755 ./oep/director-health-checks/ruler-check.sh
./oep/director-health-checks/ruler-check.sh > ./logs/director-health-checks/ruler-check.log &

wait

echo -e "\n------------------------------------------" >> result.txt

## Show results
echo -e "\n Results ***********************************************************************************";
cat result.txt;
echo -e "********************************************************************************************";