# ml-model-serving-application
fully automated infrastructure deployment to support a simple machine learning model serving application


## Prerequisites

- Python 3.8 or higher
- Docker, Docker Desktop and Docker Compose
- FastAPI installed
- Terraform (for infrastructure provisioning)
- AWS CLI configured with appropriate permissions

## Installation

2. Build and start the application:
    The building and starting of this application was orginally meant to be handled by docker compose, however due to time constraints this is not fully wokring. Instead please run the folllowing docker commands 
    ```bash
     docker build -t fastapi-ml . 
    ```
  The docker image will now be created and stored locally on your machine
  to run an instance of this image please use docker desktop. 
  Once you run an instance of the image, the application should now be available at http://0.0.0.0:8000/ on your machine.
  navigate to http://0.0.0.0:8000/docs to view the created APIs

3. Deploy infrastructure (if applicable):
    Please note that you must be logged into aws a user on your own machine before running any terraform commands
    
    In order to store images using amazon cloud an instance of Amazons ECR can be created from the terrafrom directory.

    Naviagte to this directory and run the following commands.
    ```bash
    terraform init
    terraform apply
    ```
4. The github actions workflows are contained in the .github/workflows folder of this project.
    (Not fully implemented due to time constraints)

5. Pythons tests are located in the /tests directory.
    the test file currently not fully implemented due to time constraints and an issue with pytest not finding any tests. 



