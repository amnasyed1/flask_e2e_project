FROM python:3.11-slim-buster
WORKDIR /app
COPY . /app/
RUN pip install pymysql && pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]

## FROM uses a python 3 image
## WORKDIR creates a new folder called 'app' and if it doesn't exist it makes that the working directory
## COPY copies the contents the 3 files and put them inside a new folder called application
## RUN installs the packages in the req.txt file
## EXPOSE exposes port 5000 to the operating system so it can communicate with the virtual operating system that docker created
## CMD runs the flask app
