# Docker Quiz: Questions

1. **If Docker containers are like shipping containers, what would the Docker image be?**
   - Answer: The Docker image would be like a drawing of the shipping container that shows how to build it

2. **You want to ensure your container is running fine and healthy. Which Docker feature will you use to monitor its health?**
   - Answer: We will use `healthcheck` feature

3. **If a Docker network is like a company's internal LAN, what would `docker-compose.yml` be?**
   - Answer: `docker-compose.yml` would be like a map that shows how everything should be connected

4. **You have two services, `frontend` and `backend`, and you want to ensure that `backend` starts before `frontend`. Which Docker Compose key value will you use?**
   - Answer: We will use `depends_on` key in `frontend` with `backend` as value

5. **If Docker volumes are like USB drives, what does the `volumes` key in Docker Compose do?**
   - Answer: The `volumes` key lets you share storage, like sharing toys with friends

6. **You need to create multiple instances of the same service. What feature of Docker Compose will you use?**
   - Answer: We will use `scale` feature

7. **If Docker networks are like chat rooms, what would the `bridge` network mode be?**
   - Answer: The `bridge` network mode would be like the main chat room where everyone can talk

8. **You want to limit the CPU usage of a specific container. Which Docker Compose key value will you use?**
   - Answer: We will use `deploy.resources.limits.cpus` feature

9. **If the Docker Hub is like a public library, what would `docker pull` be?**
   - Answer: `docker pull` would be like borrowing a book from the library

10. **You need to pass environment variables to a container to configure its settings. Which Docker Compose key value will you use?**
    - Answer: We will use `environment` feature

11. **If a Docker container is like a running application on your computer, what would the Dockerfile be?**
    - Answer: The Dockerfile would be like the recipe to make the container

12. **You want to make sure a container only starts if another service is successfully running. Which Docker Compose feature helps with this dependency management?**
    - Answer: `depends_on` feature helps with this dependency management

13. **If the Docker Compose file (`docker-compose.yml`) is like a party invitation list, what would the `services` section be?**
    - Answer: The `services` section would be like the list of friends coming to the party

14. **You want to share data between multiple running containers. What Docker feature will you use?**
    - Answer: We would use volumes

15. **If Docker CLI commands are like the controls on a remote control, what would `docker-compose up -d` do?**
    - Answer: `docker-compose up -d` would start everything and let it run quietly in the background, like pressing "play" on a remote and leaving the room

16. **You need to add a host device (like a GPU) to your container. Which Docker Compose key value will you use?**
    - Answer: We would use `devices` feature

17. **If Docker containers are like individual apartments, what would `docker-compose` be?**
    - Answer: `docker-compose` would be like the whole building of the apartments

18. **You want to ensure that your service only uses a specific amount of memory. Which Docker Compose key value will you use?**
    - Answer: We will use `deploy.resources.limits.memory` feature

19. **If Docker Compose networks are like different floors in a building, what would the `networks` key in the Docker Compose file be?**
    - Answer: The `networks` key would be like the stairs to see which floors are in the building

20. **You need to run a specific command every time your container starts. Which Docker Compose key value will you use?**
    - Answer: We would use `command` key 
