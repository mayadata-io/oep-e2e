# Contributing Guidelines

There can be majorly two kinds of contributors
- Writing Testcase 
- Automating Testcase

### Writing Testcase 
Usually Testcases are written by Test Architects / Leads / Engineers which will be then approved by Test Architects. The collection of these TCs is available [.master-plan.yaml](.master-plan.yaml). The format of TCs to be written in [.master-plan.yaml](.master-plan.yaml) is mentioned in [master-plan.md](master-plan.md) 



### Automating Testcases
Once the TCs are available in [master-plan.md](master-plan.md), Contributors(Automation Engineer) shall pick the *Not Automated* TCs from for automation, usually we recommend to pick based on the priority of TCs, where P0 is the highest and P3 is the lowest.

Once contributor picks the TCs, would be performing the following tasks

1. Issue would be created with [tcid] mentioned [.master-plan.yaml](.master-plan.yaml)
2. Issue would be added with label e2e-wip and e2e-test-pX, where X can have the value 0 to 3 i.e TC priority. 
3. TC automation would be termed e2e-dev-complete post the following tasks would be done
   - Readme update
   - Automation code
   - Gitlab yaml update which would be used to call TC in the pipeline
4. Review would be done by peer and merged. A label e2e-complete will be added to the issue
5. Once the TC runs successfully in the pipeline, TC status would be changed to Automated.


