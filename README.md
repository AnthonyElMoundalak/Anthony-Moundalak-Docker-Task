## Anthony El Moundalak

### New Keyword

1. **healthchecks**
Like going to the doctor to check your health, Health checks monitor the status of containers and can be used to determine if a service is healthy or not. It helps ensure that your services are running correctly and can automatically restart them if they fail.
`test`: Specifies the command to run to check the health of the service. 
`interval`: How often to run the health check (every 30 seconds).
`timeout`: The time to wait for a response before the health check is considered to have failed (10 seconds).
`retries`: The number of consecutive failures needed to consider the service as unhealthy (3 retries).


2. **command**
To override the default command for a container. Allows to specify a custom command or arguments when starting the container.
`command: server /data --console-address ":9001"`

`server /data`: This tells MinIO to start the server and use /data as the storage directory. MinIO will store its data in this directory.

`--console-address ":9001"`: This option specifies the address and port on which the MinIO console (the web-based management interface) will be accessible. In this case, it's configured to listen on port 9001 on all network interfaces.


3. **networks**
Allows you to define custom networks for your services. Networks enable containers to communicate with each other over isolated networks. You can specify network configurations such as aliases, IP addresses, and external connectivity.
`networks`: This section defines a custom network called app-network.
`app-network`: The custom network to be used by the services. The `driver` option specifies that a bridge network is being used, which is the default network type for Docker Compose.



### Instructions

**Follow these step:**
1. Clone this repo
2. Run docker-compose.yml file with this command "docker compose up --build"
3. Run the post.py file to post the image in minio
4. Open http://localhost/9001 and login to see the image saved in your bucket
5. If you want to send another photo, put the photo in ./api directory and adjust the post.py file
6. If you want to send a text file, only adjust the post.py file and put your text inside the context variable in data json variable

PS: **you can adjust your minio credentials from Dockerfile and docker-compose.yml**
Default username : access-key
Default password : secret-key
To login in minio 
