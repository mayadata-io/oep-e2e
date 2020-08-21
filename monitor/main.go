package main

import "sync"

func main() {
	initializeEnvValues()
	var wg sync.WaitGroup
	wg.Add(2)
	go poolLandingMachine()
	go poolGitlab()
	wg.Wait()
}
