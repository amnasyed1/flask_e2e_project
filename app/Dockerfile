FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]

# Docker build command: docker build -t docker_example_1 .
# Docker run command: docker run -d -p 5001:5000 docker_example_1

## FROM uses a python 3 image
## WORKDIR creates a new folder called 'app' and if it doesn't exist it makes that the working directory
## COPY copies the contents the 3 files and put them inside a new folder called application
## RUN installs the packages in the req.txt file
## EXPOSE exposes port 5000 to the operating system so it can communicate with the virtual operating system that docker created
## CMD runs the flask app