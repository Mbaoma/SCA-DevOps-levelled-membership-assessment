# Assessment 
**Note : Ensure you make a screenshot of each step detailed below but do not   upload it to your Repo until you are told to do so by the coordinators**

## Steps
-   Push all your dockerfiles and docker compose files to your repository created in L3 in a branch called - Docker and  a folder called L4-containerization) and also push your docker images  to your dockhub account 
-   Install docker on your machine 
-   Create a docker hub account ( share this with us in your submission )
-   Write a docker file that will display a webpage with a text “This is my L4 SCA DevOps assignment ” 
-   What is Docker Compose?
-   Write a docker compose file that can be used to deploy 3 containers ( kibana , nginx , and mysql ) 
-   Ensure the 3 containers are running 
List all the docker images you have running on your system 
-   Connect to your 3 running  containers  
Check all the containers running on your machine now 
-   Add a volume to your mysql so its data can persist
-   Stop the container created in 4.2.3 above 
Update the dockerfile in 4.2.3 to display a webpage with a text “ This is the V2 of my submission”  , build the image , push to dockerhub and create a container 

## Docker Commands
Checkout into the 'docker' branch
1.  Change directory into the 'L4-containerization' folder, then run the flask app
    ```
    python main.py
    ```

2.  Create the Docker image
    ```
    docker build -t mbaoma/l4-containerization:v1 .
    ```

3.  Run the docker file
    ```
    docker run -p 8888:5000 --name l4-containerization mbaoma/l4-containerization:v1
    ```

4.  To confirm if your container was built, run:
    ```
    docker ps -a
    ```

5.  View the image in your localhost port 8888 by typing ```localhost:8888``` in your browser

![image](https://user-images.githubusercontent.com/49791498/124098371-687c0b80-da54-11eb-99d5-a4aa835dd17d.png)

*Docker Container Image*

6.  Push the image to docker hub
    ```
    docker login
    docker push mbaoma/l4-containerization:v1
    ```
    The image is published on [dockerhub](https://hub.docker.com/repository/docker/mbaoma/l4-containerization)

7.  Build the docker compose file
    ```
    docker-compose up
    ```

8.  Make your changes

9.  Remove the previous docker container by running:
    ```
    docker rm -f container-id
    ```
    
10. Create the updated image, assign it a tag, 'latest'
    ```
    docker build -t mbaoma/l4-containerization:latest .
    ```
    
11. Run the docker file
    ```
    docker run -p 8888:5000 --name mbaoma/l4-containerization mbaoma/l4-containerization:latest 
    ```
    
12. Push the updated image to DockerHub
    ```
    docker push mbaoma/l4-containerization:latest 
    ```

13. View the update image in your local browser by typing ```localhost:8888```

    *Updated docker image*

    The updated image is published on [dockerhub]()

## Docker Hub Repo
The image is published on [https://hub.docker.com/repository/docker/mbaoma/l4-containerization](https://hub.docker.com/repository/docker/mbaoma/l4-containerization)