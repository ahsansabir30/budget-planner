# Devops-Project
This is the documentation for my QA DevOps Fundamental Project.

## Objective
The overall object of the project was to create an app, which had CRUD functionality and utilised atleast 2 tables which comprised at a minimum of a one to many relationship. The core structure of the application was built using a micro web framework Flask and used a MySQL database (to store data which is inputed by the end user).

## Overview
The project that I chose to create was a budget/ expense tracker, whereby the end user is able to create different plans and have different expenses within each plan. The application had to have the ability to create, read, update and delete all plans and expenses. Therefore we had to create a two tables (i.e plan and expenses) which reflected this one to many relationship, whereby one plan could have multiple different expenses.

To start the project, I started by creating an ERD diagram which reflected this relationship.
![erd diagram](https://user-images.githubusercontent.com/92265482/182646801-7e4dee1b-69ce-4081-bb3a-72f03dea4842.PNG)

However due to the timeframe allocated I was unable to add user login functionality, which meant each end-user did not have the ability to create there own personal plans and expenses. Therefore the main future goal is to add in login functionality, which will give the end user the ability to create personalised plans (and thus no chance of cross-sharing).

This relationship is reflected below, as an ERD diagram. The additional relationship created will be with the user and the plan, which reflects as a one to many relationship (between the user and his/her plans).


## Risk Assessment
Before building the projects, I had to outline some of the risk attached with building the software and to propose any measures that we could implement within the production of the app and thus, reduce/ mitigate any affects that could happen when the app is hosted. 

Some of the measures were implemented within the development of the application (and are marked in the colour green on the assessment). The intial assessment can be seen below:
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

To track the project I used Trello - which is a kanban board, that enforces the use of agile methodology. Within my project, my task started at first to breakdown user stories, and assign story points to each user story task, taking into account MoSCoW prioritisation (i.e. task which are important for task functionality). Each user story task was put in the product backlog at first and then was moved into the spring backlog (dependent on its importanct, which is reflected by its story point).     
Once its moved into the sprint backlog, each task will individually be moved into 'in progress' tab dependent on if I was working on that task or not (and then on to the review, where it had to pass an initial test).

From below you can see my Trello Kanban Board:
![kanban board](https://user-images.githubusercontent.com/92265482/182798057-6bafcb4e-4bf7-40d5-ad11-7d5109111aae.JPG)
![kanban board2](https://user-images.githubusercontent.com/92265482/182813534-fdec63f2-78d0-4ece-8bcb-91b76e6eaeec.JPG)

Within the project specification we had to utilise a CI/CD pipeline, which focuses on improving software delivery throught the software development cycle (this process had to be automated). 

To aid this CI pipeline, I used a version control system known as git and held the repository in github. Within this project serveral branches were used (Main, Develop, and Features) - which meant I was able to make changes to existing code without affect the main code. It also kept a commit history which showed the various commitments I made during the software cycle (and thus gave me different points of return in case of failure) and gave me an different enviroment to store the code.

The main project was built using Flask and a python3 enviroment, which was further hosted in its own enviroment using a GCP compute engine instance (i.e. a virtual machine). Within the project we used 3 different compute engines, these were tasked with doing different task - the first one being already mentioned above. The other two instances were used to host a WSGI server (i.e. a production server, using Gunicorn) and the other, was used to host Jenkins. 
The Jenkin was setup as a 'freestyle project', in order to create a enviroment to build our WSGI server, to automate any builds and to do any unit and intergration test after any changes on our github repo (specifically any push events on the develop branch). In order to create this automated pipeline, we had to use a webhook on the github repo, which would trigger after a 'git push' event occured on the develop branch.     

This automated pipeline and overall architecture can be seen in the diagram below:    
![image](https://user-images.githubusercontent.com/92265482/182813045-6e7dccda-bfaa-4c5c-8375-685f10ab9ce6.png)

## Testing
The testing phase of the app was built within the automated pipline spoken above (through the use of Jenkins). The test implemented within this pipeline was mainly focused around testing the CRUD functionality of the application. The two type of test impelemented within the application were integration testing (to test the forms within the application) and unit testing (to make sure the CRUD functionality worked consistently, i.e. testing each funtion within the routes file).

When we push any changes to our code into Github - a Jenkin build begins, which will test if our code passes both our unit and integration test. If the test fails, the build halts and nothing is passed on to the production server (indicating the test has failed), else the new build is passed on to the production server (where the new build application is hosted on). 
![image](https://user-images.githubusercontent.com/92265482/182799770-4f09e212-c6a7-4657-b116-a1054dff2b56.png)

However from the risk assessment, we can see that other test could have been implemented into our application to handle any flaws within our application. For example, we have not tested how our application handles high load of demand, or what would happen if a natural disaster occured or any security test. This is something that would need to be implemented if the app was deployed in a real enviroment.   

The coverage report can be seen below:

![image](https://user-images.githubusercontent.com/92265482/182799257-65c80630-e62c-4c37-ae7b-7614d513dcf7.png)

## Application
Once the build has finished, the production server is loaded and we are greeted to the home page, where we will be able to see any plans we create later on. 
![image](https://user-images.githubusercontent.com/92265482/182639387-b2992977-f45c-4fc2-a3b6-2bfbd69ee97c.png)
To create a new plan, we click the green button 'Create Plan'. This will display 2 fields where we can enter our new plan. The budget field has an extra validator which checks that for the input being only a number, and that the number follows a standard of currency format (i.e. 2 decimal places).
![image](https://user-images.githubusercontent.com/92265482/182639760-3ceb7243-896b-4d34-862d-dcd68468b0d6.png)
Once the form is completed, we can click the green button 'submit', to submit the new plan.
![image](https://user-images.githubusercontent.com/92265482/182640145-cb7177ed-1887-4e55-8c8f-3926a859f5d6.png)
We should be then redirected back to the home page, where we will see the new plan we just created earlier.
![image](https://user-images.githubusercontent.com/92265482/182640476-7548b2a3-3b84-4bf1-902a-d37d3d9be1d6.png)
Within each plan, we can add more details (i.e. any expenses that could occur under each plan). To do this we click on the plan name we are interested in, and we will be redirected to an expense page (this is where all expenses under a plan are located). 
![image](https://user-images.githubusercontent.com/92265482/182642241-6b26a58f-d159-4879-af1a-aad0e4a1a365.png)
To create a new expense we follow the same format spoken above (i.e. clicking on the green button 'create expense'). Once a new expense is created, we will be redirected back to the expense page.
![image](https://user-images.githubusercontent.com/92265482/182642857-93f5af11-7d31-49fa-b491-82634c8f38a5.png)
Once a new expense is created, the application will total up all expenses within a plan and will indicate if you are above the budget assigned to the plan (using the colour green - within budget or red - over budget)
![image](https://user-images.githubusercontent.com/92265482/182643478-3fcfa026-24d7-494d-bab6-590dfd030767.png)
Within the application all plans and expenses can be updated and deleted, which is either done by clicking on the 'delete' button in red and or clicking the 'update' button in blue.

## Future

