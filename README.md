# SimpleWebpageDocker
Today we'll be creating a simple webpage using the apache image as the base image that connects to a mysql-server container via cgi (common gateway interface) with python.

Structure:
apache
* Dockerfile
* index.html file
* python file to get the message

NOTE: The index.html file is only there to make sure apache container is successful, we'll be using the python file to edit our webpage after 

database
* Holds SQL commands to run when mysql continer is created 

docker-compose.yaml
* docker compose file that links apache and database together

# To run:
1. Download apache, database folders and docker-compose.yaml
2. In your terminal: 
	* `docker compose build` 
	* `docker compose up -d`
The -d flag is running the containers as "detached" and therefore ran in background

To destroy the containers: `docker compose down`
