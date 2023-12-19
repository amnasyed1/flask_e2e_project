# flask_e2e_project

## Web Service
The web service created is a flask application, which displays information and data pertaining to food allergies. 

The "Home" page is a greeting page to users who land on the web service. It provides a greeting and a brief summary of the application , it also directs users to visit the "About" tab to learn more about the application and data displayed on the application. The "About" page also contains a link, [foodallergy.org](https://www.foodallergy.org/living-food-allergies/food-allergy-essentials/common-allergens), which leads users to FARE's page about the 9 most common food allergens, containing details about the 9 allergens as well as more information pertaining to the topic of food allergies. 

The app has two pages worth of data, Patients and Allergy Testing.
- The Patients page, displays data in a table format about patients who have previously tested positive for a food allergy to one or more of the top 9 most common food allergens that trigger an allergic reaction according to the Food Allergy, Research, & Education (FARE) organization. The table's fields are: ID, First Name, Last Name, Date of Birth, and Gender. The ID is the primary key of the table, as each patient has their own unique ID. 
- The Allergy Testing page, displays data in a table format about the patients' allergy tests and results. Each patient listed in the Patients table was retested for a food allergy they have previously tested positive for. The fields in the Allergy Testing table are: ID, Patient ID, Test Name, Test Result, and Test Date. Each patient either had a skin prick test or blood test done to determine if they are still allergic to the allergens they had previously tested positive for. The Patient ID column is the same as the ID column in the Patients table, and the ID column in the Allergy Testing table is the ID for their tests and the test result. The primary key in the Allergy Testing table is ID, and the forigen key is Patient ID.  

## Technologies Used

To develop the Food Allergy App, I used the technologies listed below:

- GitHub - version control system

- Environment Variables - .env 

- Flask - web framework written in Python; frontend and backend

- Tailwind - frontend framework

- MySQL - database, used Azure to deploy it to the cloud

- SQLALchemy - ORM (Object Relational Mapper)

- Sentry.io -  a logger for tracking errors

- Docker -  used to containerize the app

- Azure - deployed the application to the cloud via Azure

## Steps to Run the Web Service: Locally and Deploying it to the Cloud

### Locally

### How to deploy it to the cloud

#### How could they run it without Docker locally?
#### How could they run it with Docker locally?
#### How could they deploy it to the cloud?

## Template of the .env file and its structure