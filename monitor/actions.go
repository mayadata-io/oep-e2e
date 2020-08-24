package main

import (
	"fmt"
	"os/exec"
	"strings"
)

func restartGitlabRunners() {
	_, config := loadConfig()
	for _, val := range config {
		Command := sshToRunners + val + " --command" + " 'systemctl restart gitlab-runner'" + " > /dev/null && echo true || echo false"
		output, _ := exec.Command("/bin/sh", "-c", Command).Output()
		commandOutput := (string(output))
		if strings.Contains(string(commandOutput), "true") {
			fmt.Printf(getTime()+" Restarted Runner %s\n", val)
		} else {
			fmt.Printf(getTime()+" Unable to Restarted Runner %s\n", val)
		}
	}
}

//Checks wheether IP table rules exists inside landing machine
//sshpass should be installed inside container
func isIpTablesFlushed() bool {
	Command := sshToLandingMachine + "'iptables -L'"
	output, _ := exec.Command("/bin/sh", "-c", Command).Output()
	commandOutput := (string(output))
	if strings.Contains(string(commandOutput), "master-1551782451.mayalabs.io") {
		fmt.Printf(getTime() + " IPtables EXISTS\n")
		return false
	}
	fmt.Printf(getTime() + " IPtables does not EXIST\n")
	return true
}

//Restore the IP table rules in Landing machine
func restoreIpTables() {
	fmt.Printf(getTime() + " Restoreing IPtables")
	Command := sshToLandingMachine + "'cd test && iptables-restore < ip_tables.out_26April2020'"
	exec.Command("/bin/sh", "-c", Command).Output()
}

//Checks whether ESX is reachable from landing machine or not
func isEsxRechable(esxIP string) bool {
	Command := sshToLandingMachine + "'ping -c 1 " + esxIP + " > /dev/null && echo true || echo false'"
	output, _ := exec.Command("/bin/sh", "-c", Command).Output()
	commandOutput := (string(output))
	if strings.Contains(string(commandOutput), "false") {
		fmt.Printf(getTime()+" ESX-%s is not reachable\n", esxIP)
		return false
	}
	fmt.Printf(getTime()+" ESX-%s is reachable\n", esxIP)
	return true

}

//Power on the VM inside all the available ESX
func powerOnVms() {
	config, _ := loadConfig()
	for key, _ := range config {
		if isEsxRechable(key) == true {
			fmt.Printf(getTime()+" Checking for turned off VMs in ESX-%s\n", key)
			vmId := config[key]
			for _, item := range vmId {
				powerOn(key, item)
			}
		}
	}
}

//power on the VMs inside particular ESX
func powerOn(esxIP string, vmId string) {
	Command := sshToLandingMachine + "'sshpass ssh -o StrictHostKeyChecking=no root@" + esxIP + " 'vim-cmd vmsvc/power.on " + vmId + "'" + "'" + " > /dev/null && echo true || echo false"
	output, _ := exec.Command("/bin/sh", "-c", Command).Output()
	commandOutput := (string(output))
	if strings.Contains(string(commandOutput), "true") {
		fmt.Printf(getTime()+" Powered on VM with id %s in ESX-%s\n", vmId, esxIP)
	}
}
