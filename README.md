# DevOps Project – Eva and Ryan

## Table of Content:
1.	Resources
  a.	PowerPoint
  b.	Jira Board
  c.	Git Repository
2.	Objectives and Scope
3.	Planning
  a.	Jira Board
  b.	AWS Digital Infrastructure Diagrams
  c.	Docker Structure
  d.	Risk Assessment
4.	Version Control Software: GitHub
5.	Containerisation
  a.	Docker
  b.	Docker-compose
  c.	Docker-swarm
6.	Jenkins
  a.	Webhook
  b.	CI Pipeline
7.	Testing: Unit testing
8.	Reflection
a.	Further work to be done/ stretch goals
b.	Risk Assessment Revisited 
9.	Author and Acknowledgements

## Resources:
PowerPoint: https://onedrive.live.com/view.aspx?cid=e3950bf5a5bb0c26&page=view&resid=E3950BF5A5BB0C26!1455&parId=E3950BF5A5BB0C26!106&authkey=!ANl1upi6MXPhpbk&app=PowerPoint
Jira: https://test-jira11.atlassian.net/jira/software/projects/QDP/boards/3
Git: https://github.com/RyanCD1/DevOpsProject
Initial Risk Assessment:https://onedrive.live.com/view.aspx?cid=e3950bf5a5bb0c26&page=view&resid=E3950BF5A5BB0C26!1456&parId=E3950BF5A5BB0C26!106&authkey=!ANl1upi6MXPhpbk&app=Word
Revised Risk Assessment:https://onedrive.live.com/view.aspx?cid=e3950bf5a5bb0c26&page=view&resid=E3950BF5A5BB0C26!1457&parId=E3950BF5A5BB0C26!106&authkey=!ANl1upi6MXPhpbk&app=Word

## Objectives & Scope
To successfully containerise and deploy a flask-application running in two micro-services (frontend and backend) with a managed RDS database server and a Continuous Integration (CI) pipeline that tests the application. A Jenkins webhook should be used so that every time new code is pushed to git the application is tested, built, and deployed again. The application must make use of a reverse-proxy server to make the application accessible to users.

## Planning
### Jira Board
The Jira board for the project is linked above – it contains the user stories, smart commits, prioritisation, a sprint, a Kanban board, story points, task allocation and a linked Git repository. We planned the task and broke the project into three Epics and 15 issues:

![image](https://user-images.githubusercontent.com/86105248/132007034-d46714f6-1420-46d2-b76e-d8fb021493b1.png)
 
These issues were placed into one sprint and worked on across the Kanban board:
 
 ![image](https://user-images.githubusercontent.com/86105248/132007081-290b59cb-32f8-48f9-8719-3841ddae200d.png)

For these issues we used smart commits to keep track of our progress:

![image](https://user-images.githubusercontent.com/86105248/132007098-c9751df9-d4e0-4450-9cd7-fb71ff3a3c6d.png)
 
The Jira board was used for initial planning and work distribution and then continually updated throughout the project to reflect progress and keep track of development.

### AWS Structure
#### VPC, Subnets, and Security Groups
A VPC was set up through AWS with separate security groups for the manager and worker nodes, as well as the RDS database. The Manager and Worker nodes allow port access within the VPC security group, port 8080 general access to Jenkins (but with login protection via password and username) and general HTTP requests from anywhere. The Database security allows traffic only from within the VPC security groups on port 3306. 
 
![image](https://user-images.githubusercontent.com/86105248/132007120-c7aa5de7-db40-429a-af10-591a61017cd3.png)

Digital Infrastructure Diagrams:
As part of the planning process, we made changes to reflect conflicts and difficulties in setups and a desire to increase security through use of the managed database server on a private subnet. This layout structure evolved into the final product:

![image](https://user-images.githubusercontent.com/86105248/132007138-3d59b49d-2a6a-4c6a-a871-0ad2774b37ef.png)

(Amazon RDS, 2021)

### Docker Structure:
We used docker as our containerisation software. The application deploys on docker-swarm across one swarm-manager and three worker nodes.
We chose this configuration to improve scalability and offer increased redundancy as individual nodes can break without damaging the app as a whole with the swarm-network set-up.
### Risk Assessment:
We completed an initial risk assessment at the beginning of the project where we brainstormed potential risks we could run into and steps we might take to mitigate them:

 ![image](https://user-images.githubusercontent.com/86105248/132007164-3680fd50-151e-4650-a622-c910e512a464.png)

Link: https://onedrive.live.com/view.aspx?cid=e3950bf5a5bb0c26&page=view&resid=E3950BF5A5BB0C26!1456&parId=E3950BF5A5BB0C26!106&authkey=!ANl1upi6MXPhpbk&app=Word

## Version Control Software - GitHub
GitHub link: https://github.com/RyanCD1/DevOpsProject
We used Git for version control and connected our Git repository to Jira, to link our development process to the tasks we were working through, and to Jenkins to set up a Webhook that Jenkins builds, tests and deploys any changes made in the code base.

## Containerisation
### Docker
Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package. These are defined inside Dockerfiles. The application was initially built in basic docker in order to build familiarity and learn how the different parts inter-connected. Once this was running, the application was moved to Docker-compose, and then on to Docker Swarm. This allowed the containerisation and image building of the application to happen manually at first, before moving onto automatic deployment. This was found to be beneficial, as it allowed intimate control of the builds while in the testing phase. 
### Docker-compose
Docker compose is a tool installed alongside docker, offering a smoother containerisation experience managed through a .yaml file. Docker-compose automatically places the services created into the same network allowing for communication between containers without having to manually set up the network.
Docker-compose configuration: 

![image](https://user-images.githubusercontent.com/86105248/132007400-2378030f-f0ba-49da-be49-186198b907a2.png)

### Swarm
Docker-swarm allows the docker-compose images to be pulled down from docker-hub and deployed across manager and worker nodes that connect together to increase reliability and offer easier scaling. The Jenkins CI Pipeline deploys new changes to the code-base in docker swarm configuration across one manager and three workers.
Docker-swarm configuration:

![image](https://user-images.githubusercontent.com/86105248/132007451-a84c208e-2f41-4a53-a910-37de693a207f.png)

## Jenkins
### Webhook
We linked Jenkins to the Git repository and set up a pipeline so that new code changes were pushed from git to Jenkins and then tested, built, and deployed by Jenkins on the VMs, updating the application. 
Image of a successful Webhook build:
 
 ![image](https://user-images.githubusercontent.com/86105248/132007486-1daa36d7-fbbe-4863-bd3c-c41ce3ed0f92.png)

### Continuous Integration Pipeline
Jenkins is a free and open source automation server. It helps automate software development related to building, testing, and deploying, facilitating continuous integration and deployment.
For this project, the stages of the Jenkins pipeline are as follows:
•	Installation – Installing all prerequisites onto the local machine to run the rest of the containers
•	Testing - Which produces coverage reports on the console
•	Build and push images - Docker-compose is used to build the images and push them to Docker-Hub
•	Deploy stack - Configures the web-application on the manager and worker nodes
Image of the Jenkinsfile:
 
![image](https://user-images.githubusercontent.com/86105248/132007519-fbf0f465-fae1-4f5b-a583-d37656a02720.png)

## Testing: Unit testing
The testing can be run manually for 100% coverage for both the frontend and backend:
This same testing process is integrated into the Jenkinsfile and Webhook deployment process to test every new build of the application and produce coverage reports that are displayed as an artefact of the build:
 
 ![image](https://user-images.githubusercontent.com/86105248/132007540-cb346de8-ec42-47f8-ae47-7071ed83354b.png)

These coverage reports both demonstrate 100% coverage for the front and back ends respectively: 
Frontend:
 
![image](https://user-images.githubusercontent.com/86105248/132007563-8c965afb-9bff-4f2d-91b3-d77a0eabddac.png)

Backend:
 
![image](https://user-images.githubusercontent.com/86105248/132007577-0a599c87-d133-4326-a88b-113ad3b4a6f9.png)

## Reflections
### Risk Assessment
We updated our risk assessment matrix as we progressed throughout the project and new risks became apparent and offered final reflections on the way each risk was handled throughout the project and the level of threat they would pose going forward if the application were to continue to be run:
 
![image](https://user-images.githubusercontent.com/86105248/132007609-41f189e8-0aa6-4fec-aebc-079a80ccd461.png)

Link: https://onedrive.live.com/view.aspx?cid=e3950bf5a5bb0c26&page=view&resid=E3950BF5A5BB0C26!1457&parId=E3950BF5A5BB0C26!106&authkey=!ANl1upi6MXPhpbk&app=Word

###Further work to be done/ stretch goals
1.	Add another manager node to improve reliability and safeguard against errors with a single manger bringing the application down
2.	Extend knowledge into extra tools – Kubernetes, Terraform, Ansible
## Author and Acknowledgements
Grateful acknowledgement to Luke Benson for imparting all the necessary DevOps knowledge. Team 1 remains the greatest team. Project by Ryan Donaghue and Eva Bullman.
