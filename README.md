# flask_e2e_project

## Web Service
The web service created is a flask application, which displays information and data pertaining to food allergies. 

The "Home" page is a greeting page to users who land on the web service. It provides a greeting and a brief summary of the application , it also directs users to visit the "About" tab to learn more about the application and data displayed on the application. The "About" page also contains a link, [foodallergy.org](https://www.foodallergy.org/living-food-allergies/food-allergy-essentials/common-allergens), which leads users to FARE's page about the 9 most common food allergens, containing details about the 9 allergens as well as more information pertaining to the topic of food allergies. 

The app has two pages worth of data, Patients and Allergy Testing.
- The Patients page, displays data in a table format about patients who have previously tested positive for a food allergy to one or more of the top 9 most common food allergens that trigger an allergic reaction according to the Food Allergy, Research, & Education (FARE) organization. The table's fields are: ID, First Name, Last Name, Date of Birth, and Gender. The ID is the primary key of the table, as each patient has their own unique ID. 
- The Allergy Testing page, displays data in a table format about the patients' allergy tests and results. Each patient listed in the Patients table was retested for a food allergy they have previously tested positive for. The fields in the Allergy Testing table are: ID, Patient ID, Test Name, Test Result, and Test Date. Each patient either had a skin prick test or blood test done to determine if they are still allergic to the allergens they had previously tested positive for. The Patient ID column is the same as the ID column in the Patients table, and the ID column in the Allergy Testing table is the ID for their tests and the test result. The primary key in the Allergy Testing table is ID, and the forigen key is Patient ID.  

Screenshots of the Home, About, Patients, and Allergy Testing pages are all in the `docs` folder within the folder `screenshots`. 

## Technologies Used

To develop the Food Allergy App, I used the technologies listed below:

- GitHub - version control system

- Environment Variables - .env 

- Flask - web framework written in Python; frontend and backend

- Tailwind - frontend framework

- MySQL - database, used Azure to deploy it to the cloud

- SQLALchemy - ORM (Object Relational Mapper)

- API service - the api endpoint is hosted within Flask's backend

- Sentry.io -  a logger for tracking errors

- Docker -  used to containerize the app

- Azure - deployed the application to the cloud via Azure

## Steps to Run the Web Service: Locally or Deploying it to the Cloud
The web service can be deployed through various methods: locally (without Docker), locally using Docker, and deploying it to the cloud through using Azure.

### Locally:
1. Clone the GitHub repository into your local environment by using using `git clone https://github.com/amnasyed1/flask_e2e_project.git`
2. Next, navigate into the `app` folder in the terminal by using `cd flask_e2e_project/`.
3. Create a ``.env`` file and populate it with your credentials, and ensure that there is a ``.gitignore`` file in the same directory as the app.py file and .env file. The .gitignore should have ``.env`` written within the file for it to work.
4. Finally, to run the flask app, use `python app.py`. The terminal will populate a link which may look similar to `Running on http://127.0.0.1:5000` and click it. Once, you click the link you will be directed to the Food Allergy App!

### Locally using Docker:
1. To run the flask app locally using Docker, ensure your `app` folder has both a ``Dockerfile`` and a ``docker-compose.yaml`` file.
2. In the terminal, type `docker-compose build` to build the images within the flask apps.
3. After that, to run the images in the containers, type `docker-compose up`.
4. Next, to run the image `docker run -p <newport:oldport> <name of image>`
   - "-p" is the port; if you would like to run the image on a port different from the one you exposed in the Dockerfile and documented in the app.py, then write the new port, then a colon`:` and then the old port. For example (-p 5001:5000)
5. To preview the image, click `Web Preview`, `Change Port`, enter the new port number, for instance, utilizing the example above, type `5001` and then click `Change and Preview`, and your image will be run in a container and can be viewed without any issues.
6. Next, in the terminal type `docker-compose ps` to see the information in a list/table structure with contents such as the container ID, image name, command, when it was created, the status, ports its exposed on etc.

In the `docs` folder, within the `screenshots` folder, you can see the flask app dockerized and running on the new port 5001, as well as the docker images I created in the terminal.


### Deploy the Flask App to the Cloud (Azure):
1. In your Google Cloud Shell terminal, install Azure CLI by typing in this command `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash` and hit enter.
2. After that type `az login --use-device-code` to log in. After you hit enter a link will be provided with an authentication code, copy the authentication code, click the link, sign in with your emial, and paste the authentication code.
3. Next, create a resource group. Use the command `az group create --name <create a resource group name> -- location eastus`.
4. Lastly, to deploy the app use the command  `az webapp --resource-group <groupname> --name <app-name> --runtime <PYTHON : 3.9 > --sku <B1>`. Alternately, you can also use the following command `az webapp up --resource-group <groupname>--name <app-name> --sku F1`. 

For more in-depth documentation you can visit [this link](https://learn.microsoft.com/en-us/cli/azure/webapp?view=azure-cli-latest). 

The link to my deployed Flask app is https://foodallergyapp.azurewebsites.net/. You can view how the deployed app looked like as well as further information about the deployed flask in the `docs` folder within the `screenshots folder`. 

## Template of the .env file 
``````
DB_HOST =
DB_DATABASE = 
DB_USERNAME = 
DB_PASSWORD = 
DB_PORT = 
DB_CHARSET = 
``````