package main

import (
	"fmt"
	"os"
	"strconv"
)

var (
	landingMachineIP       string
	landingMachineUser     string
	sshPort                string
	gitlabUrl              string
	landingMachinePassword string
	sshToLandingMachine    string
	sshToRunners           string
	zone                   string
	gcpPojectID            string
	poolInterval           int //Pooling time interval in sec
)

//ESX-to-VM mapping
func loadConfig() (map[string][]string, []string) {
	vmMapping := map[string][]string{
		"10.21.1.1": []string{"1", "2"},
		"10.22.1.1": []string{"15", "16", "17", "18", "19", "20"},
		"10.51.1.1": []string{"27", "28", "29", "30", "31", "32"},
		"10.58.1.1": []string{"7", "8"},
	}
	runners := []string{"aws-pipeline-runner", "k8s-native-gitlab-runner", "konvoy--istaller-autoscalar", "openshift-autoscalar"}
	return vmMapping, runners
}

//Fetches all the supported Envirnment varibles
func initializeEnvValues() error {
	var err error
	landingMachineIP, err = getEnv("LANDING_MACHINE_IP")
	if err != nil {
		return err
	}
	landingMachineUser, err = getEnv("LANDING_MACHINE_USER")
	if err != nil {
		return err
	}
	sshPort, err = getEnv("SSH_PORT")
	if err != nil {
		return err
	}
	gitlabUrl, err = getEnv("GITLAB_URL")
	if err != nil {
		return err
	}
	landingMachinePassword, err = getEnv("LANDING_MACHINE_PASSWORD")
	if err != nil {
		return err
	}
	gcpPojectID, err = getEnv("PROJECT_ID")
	if err != nil {
		return err
	}
	zone, err := getEnv("ZONE")
	if err != nil {
		return err
	}
	tmppoolInterval, err := getEnv("POOL_TIME")
	if err != nil {
		return err
	}
	poolInterval, err = strconv.Atoi(tmppoolInterval)
	if err != nil {
		return err
	}
	sshToLandingMachine = "sshpass" + " -p" + landingMachinePassword + " ssh -o StrictHostKeyChecking=no " + landingMachineUser + "@" + landingMachineIP + " -p " + sshPort + " "
	sshToRunners = "gcloud compute ssh --project " + gcpPojectID + " --zone " + zone + " root@"
	return nil
}

func getEnv(key string) (string, error) {
	value := os.Getenv(key)
	if len(value) == 0 {
		return "", fmt.Errorf("ENV %s not found", key)
	}
	return value, nil
}
