package main

import (
	"fmt"
	"net/http"
	"os/exec"
	"strings"
	"time"
)

func poolGitlab() {
	errReport, unreachable, reachable := false, false, false
	for true {
		resp, err := http.Get(gitlabUrl)
		if err != nil {
			fmt.Println(getTime()+" ", err)
			time.Sleep(10 * time.Second)
			//action performed when gitlab is down(based on variable errReport) will not be repeated.
			if errReport == false {
				if isIpTablesFlushed() == true {
					restoreIpTables()
				}
				powerOnVms()
				errReport = true
				reachable = false
			}

		}
		if resp != nil {
			if resp.StatusCode != 200 {
				if unreachable == false {
					fmt.Printf(getTime()+" Gitlab is down with status code: %d\n", resp.StatusCode)
					if isIpTablesFlushed() == true {
						restoreIpTables()
					}
					powerOnVms()
					unreachable = true
					reachable = false
				}
			}
			//Condition when Gitlab is up
			if resp.StatusCode == 200 {
				if reachable == false {
					fmt.Printf(getTime()+" Gitlab is Up with status code: %d\n", resp.StatusCode)
					if unreachable == true || errReport == true {
						restartGitlabRunners()
					}
					errReport = false
					unreachable = false
					reachable = true
				}
			}
		}
		time.Sleep(time.Duration(poolInterval) * time.Second)
	}
}

func isLandingMachineReachable() bool {
	Command := "ping -c 1" + " " + landingMachineIP + " > " + "/dev/null && echo true || echo false"
	output, _ := exec.Command("/bin/sh", "-c", Command).Output()
	commandOutput := (string(output))
	if strings.Contains(string(commandOutput), "false") {
		return false
	}
	return true
}

func poolLandingMachine() {
	unreachable, reachable := false, false
	for true {
		if isLandingMachineReachable() == false {
			if unreachable == false {
				fmt.Println(getTime(), "landing machine is not reachable")
				unreachable = true
				reachable = false
			}
		} else {
			if reachable == false {
				fmt.Println(getTime(), "landing machine is reachable")
				if isIpTablesFlushed() == true {
					restoreIpTables()
					powerOnVms()
				}
				reachable = true
				unreachable = false
			}
		}
		time.Sleep(time.Duration(poolInterval) * time.Second)
	}
}

func getTime() string {
	currentTime := string(time.Now().Format("2006-01-02 15:04:05"))
	formatTime := "[" + currentTime + "]"
	return formatTime
}
