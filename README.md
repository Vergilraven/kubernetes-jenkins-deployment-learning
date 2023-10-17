# Inventory-name: k8s-master-jenkins-deployment-selfuse-template
## k8s-master-jenkins-deployment 
## Step1: Upload yaml file  
`Upload the correct jenkins-deployment yaml files to the repository.`

## Step2: Try again
`Architecture Master: Approval the PR but have no permission managment,anyone in the organization can merge pull request`

##
`Architecture Master: This deploy project should be finished in one week`
##

## Step3: Install the regluar plugins
`Deployment Master: install the plugins in the market`

`Deployment Master: something wrong occur on the kubernetes cluster,can't enter the pod service,i would hang on.`

`Deployment Master: write test-service pipeline`

`Deployment Master: Have some difficulty can't be sloved,the issues about how to enter a running pod,and the next issue is don't find a correct method to use nat on k8s cluster，and the original plan would be delayed`

`Deployment Master: Have sloved the issues about how to enter the jenkins pods by using the following instructions`
```
sudo kubectl exec -it jenkins-5f55476864-5bznw --namespace=automated-tools /bin/bash
```

`Architecture Master: Well done,have done the excellent job,congratulations!!!`

`Deployment Master: Handle with the apt source file issues`

use the instructions following
First,bakup the source file
Second,edit the source file and copy back to the jenkins running pod 
```
sudo kubectl cp automated-tools/jenkins-5f55476864-5bznw:/usr/share/doc/apt/examples/sources.list /tmp/bakup/sources.list-bak
# Also make sure there should be two files exsits
cp -r sources.list-bak sources.list
```

<br>pipeline</br>

## Step4: Configure the code repository 

crenditals

## Step5: 
`Development Master: After Deployment Master finished the jenkins service deployment,i will use algorithms to develop our QTsys analysis,and use python3 scripts to create database including the tablename on the RDS instance`