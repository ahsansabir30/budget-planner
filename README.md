# Devops-Project
## Objective
The overall object of the project was to create an application in Flask (mircoweb framework) which utilised a CI/CD pipeline. The application had to have CRUD functionality (CREATE, READ, UPDATE, DELETE), atleast two tables which compromised a one to many relationship and used a MySQL database. 
 
## Overview
The project that I chose to create was a budget/ expense tracker, whereby the end user is able to create different plans and have different expenses within each plan. The application had to have the ability to create, read, update and delete all plans and expenses. Therefore we had to create two tables (i.e plan and expenses) which reflected this one to many relationship, whereby a plan can have multiple expenses. 
 
To start the project, I created an ERD diagram which reflected the relationship talked above.
![image](https://user-images.githubusercontent.com/92265482/182816305-41502e1d-fb9e-4de6-bf43-12720edbf58c.png)
 
However due to the timeframe allocated I was unable to add user login functionality, which meant each end-user did not have the ability to create their own personal plan with its own expenses. Therefore the main future goal is to add in login functionality, which will give the end user the ability to create personalised plans (and thus no chance of cross-sharing).
 
This relationship is reflected below, as an ERD diagram. The additional relationship created will be with the user and the plan. This is again reflected as a one to many relationship between the user and his/her plans.
![image](https://user-images.githubusercontent.com/92265482/182816683-2f5ac4e3-b53f-4692-8388-51875d13bb3b.png)
 
## Risk Assessment
Before building the projects, I had to outline some of the risks attached with building the software and to propose any measures that we could implement within the production of the app. The reason for this is, to reduce/ mitigate any effects that could happen when the app is hosted (and to avoid any future suprises).
 
Some of the measures that were implemented within the development of the application are marked in the colour green on the assessment sheet. The initial assessment can be seen below:
![image](https://user-images.githubusercontent.com/92265482/182797753-b99edb8b-e6c5-4943-8ab2-7cdf99b49361.png)
 
## Technologies
The technology stack used within this project is as follow:
- Trello
- Database GCP SQL server
- Python
- Flask
- Pytest
- Selenium
- Gunicorn
- Git
- Jenkins
- VM: GCP Compute Engine
 
To track the project I used Trello - this is a kanban board that enforces the use of agile methodology. To start this project, I had to breakdown each user story into different task (this can be seen in the kanban board below) and then I had to assign different story points, taking into account MoSCoW prioritisation (i.e. tasks which are important for task functionality, have a greater story point).
Each user story task was put in the product backlog at first and then was moved into the sprint backlog (dependent on its importance, which is reflected by its story point).    
Once it's moved into the sprint backlog, each task will individually be moved into the 'in progress' tab depending on if I was working on that task or not (and then on to the review, where it had to pass an initial test, which was done by me).
 
From below you can see my Trello Kanban Board:
![kanban board](https://user-images.githubusercontent.com/92265482/182798057-6bafcb4e-4bf7-40d5-ad11-7d5109111aae.JPG)
![kanban board2](https://user-images.githubusercontent.com/92265482/182813534-fdec63f2-78d0-4ece-8bcb-91b76e6eaeec.JPG)
 
Within the project specification we had to utilise a CI/CD pipeline, which focused on improving software delivery throughout the software development cycle (this process had to be automated).
 
Therefore, to aid this CI pipeline, I used a version control system known as git and held the repository in github. Within this project several branches were used (Main, Develop, and Features) - which meant I was able to make changes to existing code without affecting the main code. It also kept a commit history which showed the various commitments I made during the software cycle (and thus gave me different points of return in case of failure) and further to this, gave me a different environment to store the code and edit.
 
The main project was built using Flask and a python3 environment, which was further hosted in its own environment using a GCP compute engine instance (i.e. a virtual machine). Within the project we used 3 different compute engines, these were tasked with doing different task - the first one being already mentioned above. The other two instances were used to host a WSGI server (i.e. a production server, using Gunicorn) and the other, was used to host Jenkins.

To create our CI pipeline, we used Jenkins. Jenkins was set up as a 'freestyle project', in order to create an environment to build our WSGI server, to automate any builds and to do any unit and integration test after any changes were pushed on to our github repo (specifically any push events on the develop branch). In order to create this automated pipeline, we had to use a webhook on the github repo, which would trigger a jenkins build after a 'git push' event occurred on the development branch.    
 
This automated pipeline and overall architecture can be seen in the diagram below:    
![image](https://user-images.githubusercontent.com/92265482/182813045-6e7dccda-bfaa-4c5c-8375-685f10ab9ce6.png)
 
## Testing
The testing phase of the app was built within the automated pipeline spoken above (through the use of Jenkins). The test implemented within this pipeline was mainly focused around testing the CRUD functionality of the application. The two types of test implemented within the application were integration testing (to test the forms within the application) and unit testing (to make sure the CRUD functionality worked consistently, i.e. testing each function within the routes file).
 
When I pushed any changes to the code into our Github repo - a Jenkin build begins, which will test if our code passes both our unit and integration test. If the test fails, the build halts and nothing is passed on to the production server (indicating the test has failed), else the new build is passed on to the production server (where the new build application is hosted on).
![image](https://user-images.githubusercontent.com/92265482/182799770-4f09e212-c6a7-4657-b116-a1054dff2b56.png)
 
However from the risk assessment, we can see that other test could have been implemented into our application to handle any flaws within our application. For example, we have not tested how our application handles high load of demand, or what would happen if a natural disaster occured or any security test. This is something that would need to be implemented if the app was deployed in a real environment.  
 
The coverage report can be seen below:
 
![image](https://user-images.githubusercontent.com/92265482/182799257-65c80630-e62c-4c37-ae7b-7614d513dcf7.png)
 
## Application
Once the build has completed, the production server is updated and we are greeted to the home page, where we will be welcomed to the plans page (this page will show all plans that are created within the application).
![image](https://user-images.githubusercontent.com/92265482/182639387-b2992977-f45c-4fc2-a3b6-2bfbd69ee97c.png)
To create a new plan, we click the green button 'Create Plan'. This will display 2 fields where we can enter our new plan. The budget field has an extra validator, this will checks if the input is a number, and that the number follows a currency format (i.e. 2 decimal places).
![image](https://user-images.githubusercontent.com/92265482/182639760-3ceb7243-896b-4d34-862d-dcd68468b0d6.png)
Once the form is completed, we can click the green button 'submit', to submit the new plan.
![image](https://user-images.githubusercontent.com/92265482/182640145-cb7177ed-1887-4e55-8c8f-3926a859f5d6.png)
We should be then redirected back to the home page, where we will see the new plan we just created earlier.
![image](https://user-images.githubusercontent.com/92265482/182640476-7548b2a3-3b84-4bf1-902a-d37d3d9be1d6.png)
Within each plan, we can add more details (i.e. any expenses that could/should occur under each plan). To do this we click on the plan name we are interested in, and we will be redirected to an expense page (this is where all expenses under each plan are located).
![image](https://user-images.githubusercontent.com/92265482/182642241-6b26a58f-d159-4879-af1a-aad0e4a1a365.png)
To create a new expense we follow the same format spoken above (i.e. clicking on the green button 'create expense'). Once a new expense is created, we will be redirected back to the expense page.
![image](https://user-images.githubusercontent.com/92265482/182642857-93f5af11-7d31-49fa-b491-82634c8f38a5.png)
Once a new expense is created, the application will total up all expenses within a plan and will indicate if you are above the budget assigned to the plan (using the colour green - within budget or red - over budget)
![image](https://user-images.githubusercontent.com/92265482/182643478-3fcfa026-24d7-494d-bab6-590dfd030767.png)
Within the application all plans and expenses can be updated and deleted, which is either done by clicking on the 'delete' button in red to delete and or clicking the 'update' button in blue to update.
 
## Future
Overall the project creates various plans and under each plan, we can create a variety of different expenses. However the need of creating a user and being able to login/logout is extremely critical and evident in making the application ready for deployment. Therefore in future updates or sprints I would like to create additional functionality by creating a page where users can login and logout, which consequently will allow them to create their own personalised plans.
 
In addition to this, if such an update did occur in the future, it will require additional testing, mainly focused around security, as we are now including personal information and passwords.
