---
id: kubera-e2e-release-2-0
title: Kubera E2E Release 2.0
sidebar_label: Kubera E2E 2.0
---

## RELEASE NOTES
This is the 4th release of Kubera end to end (E2E) pipelines. Team continued their focus on stabilising Rancher pipeline. In this release, we are close to marking Rancher E2E as a stable pipeline alongside AWS & KONVOY E2E. We plan to observe Rancher E2E for another month before tagging it as stable.

Team continues to work on these projects:
- https://github.com/mayadata-io/kubera-api-testing
- https://github.com/dokc/continuous-kubernetes

### kubera-api-testing
This has enabled E2E to test various combinations which was previously not possible. It does so by leveraging Golang table driven testing techniques. Needless to say E2E can test `positive`, `negative`, `boundary`, `scale up`, `scale down`, etc. testcases using this simple, readable & extensible approach.

Following is an excerpt taken from the project that showcases different scenarios used to test DMAAS' add credential feature:
```go
    "aws bucket with all details": {
        CloudProvider: "aws",
        Name:          "aws-dmaas-test",
        AccessID:      awsAccessID,
        SecretKey:     awsSecretKey,
    },
    "aws bucket with duplicate name": {
        CloudProvider: "aws",
        Name:          "aws-dmaas-test",
        AccessID:      awsAccessID,
        SecretKey:     awsSecretKey,
    },
    "aws bucket with name length less than 6 character": {
        CloudProvider: "aws",
        Name:          "awsdm",
        AccessID:      awsAccessID,
        SecretKey:     awsSecretKey,
    },
    "aws bucket with name length more than 25 character": {
        CloudProvider: "aws",
        Name:          "aws-dmaas-test-backup-restore-cred",
        AccessID:      awsAccessID,
        SecretKey:     awsSecretKey,
    },
    "aws bucket without name": {
        CloudProvider: "aws",
        AccessID:      awsAccessID,
        SecretKey:     awsSecretKey,
        IsError:       true,
    },
    "aws bucket without accessID ": {
        CloudProvider: "aws",
        Name:          "aws-cred-neg",
        SecretKey:     awsSecretKey,
        IsError:       true,
    },
    "aws bucket without secretKey": {
        CloudProvider: "aws",
        Name:          "aws-cred-neg",
        AccessID:      awsAccessID,
        IsError:       true,
    },
    "aws bucket without name, accessID & secretKey": {
        CloudProvider: "aws",
        IsError:       true,
    },
    "cloudian bucket with all details": {
        CloudProvider: "cloudian",
        Name:          "cloudian-dmaas-test",
        AccessID:      cloudianAccessID,
        SecretKey:     cloudianSecretKey,
    },
    "cloudian bucket with duplicate name": {
        CloudProvider: "cloudian",
        Name:          "cloudian-dmaas-test",
        AccessID:      cloudianAccessID,
        SecretKey:     cloudianSecretKey,
    },
    "cloudian bucket with name length less than 6 character": {
        CloudProvider: "cloudian",
        Name:          "cldm",
        AccessID:      cloudianAccessID,
        SecretKey:     cloudianSecretKey,
    },
    "cloudian bucket with name length more than 25 character": {
        CloudProvider: "cloudian",
        Name:          "cloudian-dmaas-test-backup-restore-cred",
        AccessID:      cloudianAccessID,
        SecretKey:     cloudianSecretKey,
    },
    "cloudian bucket without name": {
        CloudProvider: "cloudian",
        AccessID:      cloudianAccessID,
        SecretKey:     cloudianSecretKey,
        IsError:       true,
    },
    "cloudian bucket without accessID": {
        CloudProvider: "cloudian",
        Name:          "cloudian-cred-neg",
        SecretKey:     cloudianSecretKey,
        IsError:       true,
    },
    "cloudian bucket without secretKey": {
        CloudProvider: "cloudian",
        Name:          "cloudian-cred-neg",
        AccessID:      cloudianAccessID,
        IsError:       true,
    },
    "cloudian bucket without name, accessID & secretKey": {
        CloudProvider: "cloudian",
        IsError:       true,
    },
    "minio bucket with all details": {
        CloudProvider: "minio",
        Name:          "minio-dmaas-test",
        AccessID:      minioAccessID,
        SecretKey:     minioSecretKey,
    },
    "minio bucket with duplicate name": {
        CloudProvider: "minio",
        Name:          "minio-dmaas-test",
        AccessID:      minioAccessID,
        SecretKey:     minioSecretKey,
    },
    "minio bucket with name length less than 6 character": {
        CloudProvider: "minio",
        Name:          "minio",
        AccessID:      minioAccessID,
        SecretKey:     minioSecretKey,
    },
    "minio bucket with name length more than 25 character": {
        CloudProvider: "minio",
        Name:          "minio-dmaas-test-backup-restore-cred",
        AccessID:      minioAccessID,
        SecretKey:     minioSecretKey,
    },
    "minio bucket without name": {
        CloudProvider: "minio",
        AccessID:      minioAccessID,
        SecretKey:     minioSecretKey,
        IsError:       true,
    },
    "minio bucket without accessID": {
        CloudProvider: "minio",
        Name:          "minio-cred-neg",
        SecretKey:     minioSecretKey,
        IsError:       true,
    },
    "minio bucket without secretKey": {
        CloudProvider: "minio",
        Name:          "minio-cred-neg",
        AccessID:      minioAccessID,
        IsError:       true,
    },
    "minio bucket without name, accessID & secretKey": {
        CloudProvider: "minio",
        IsError:       true,
    },
```

### continuous-kubernetes
Work is in progress to get the first E2E badge out. This first badge is all about validating Cassandra on OpenEBS.

### What's next?
Team plans to create a disposable Rancher cluster in the cloud. This on-demand provisioning  reduces the need to use Rancher E2E pipeline for one off testing purposes. In addition, this enables Kubernetes platform itself as a tunable to build the desired infrastructure to run E2E tests.

### Roadmap
E to E team need to tackle lot of unknowns like:
- Pipeline does not help in identifying the root cause of errors
- Inability to run the testcases outside of the pipeline infrastructure
- Pipelines take longer times to execute (3 to 5 hours)
- Infrastructure setup is not declarative making it hard to maintain

#### E to E team will continue to focus on the following
- Develop or use declarative tools to:
    - setup & dispose Kubernetes clusters
    - exercise granular control to run tests, stages & pipelines
    - write integration as well as e2e test cases
    - find the root cause of errors in the pipelines
    - to analyse current state of release from E2E metrics
- Implement e2e test cases from users' view of the world
  - i.e. validate & verify managing workloads on Kubera
    - Run Day 0, Day 1, and Day 2 operations
    - Run performance benchmarks
    - Provide best practices guidelines w.r.t workloads
  - In short, think & act like a Kubernetes SRE
- Be Kubernetes advocates for CI CD as well as workloads

### Appendix
- E2E - End to End
- E to E - End to End