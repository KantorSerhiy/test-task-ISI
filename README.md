# Test-Task-ISI
Test task for ISI-technology

### Installing using GitHub

Run the commands below:
````shell
git clone https://github.com/KantorSerhiy/test-task-ISI.git
python -m venv venv
venv\Scripts\activate (on Windows)
venv\bin\activate (on Linux)
pip install -r requirements.txt
python manage.py migrate
pytnon manage.py loaddata data.json 
python manage.py runserver
````


### You can run project using Docker 
Docker should be installed on your machine.

````shell
docker-compose up --build
````

#### Getting access

 - Admin (username:admin, pass: admin)
 - testUser(username:testUser, pass:1qasVGY&1)

You can create own superuser or user:)

## Endpoints

Create thread
````
http://127.0.0.1:8000/api/threads/create/
````
Delete thread
````
http://127.0.0.1:8000/api/threads/<int:pk>/delete/
````
List threads
````
http://127.0.0.1:8000/api/threads/
````
Message list 
````
http://127.0.0.1:8000/api/threads/<int:thread_id>/messages/
````
Message Create
````
http://127.0.0.1:8000/api/threads/message/create/
````
Read messages
````
http://127.0.0.1:8000/api/threads/<int:thread_id>/messages/read/
````
Unread messages
````
http://127.0.0.1:8000/api/unread/
````
Admin panel
````
http://127.0.0.1:8000/admin
````
Get JWT token
````
http://127.0.0.1:8000/api/token/
````
Refresh token
````
http://127.0.0.1:8000/api/token/refresh/
````
Verify token
````
http://127.0.0.1:8000/api/token/virify/
````

additional

Doc swagger
````
http://127.0.0.1:8000/api/doc/swagger/
````