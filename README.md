Anthony El Moundalak

1- Clone this repo
2- Run docker-compose.yml file with this command "docker compose up --build"
3- Run the post.py file to post the image in minio
4- Open http://localhost/9001 and login to see the image saved in your bucket
5- If you want to send another photo, put the photo in ./api directory and adjust the post.py file
6- If you want to send a text file, only adjust the post.py file and put your text inside the context variable in data json variable

