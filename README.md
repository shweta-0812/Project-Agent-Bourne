# Project AGENT-BOURNE
An agent which can get your tasks done. Your personal assistant.

The backend uses Python version 3.12.2 

To run backend server:


Make sure to setup and run Postgres DB on localhost:
1. Install Postgres DB
2. Install Postgres client
3. Create a DB with name 'agent_bourne'
4. Create username and password

To do the above steps run the following commands in terminal after installing Postgres:
`$ psql`
`$ CREATE DATABASE agent_bourne;`
`$ CREATE USER agent_bourne WITH PASSWORD 'your-password';`
`$ \q`

Create .env file in the root folder `backend/.env`
1. Copy sample.env to .env
2. update the values of the variables

Make sure to create migrations for DB changes
4. Make sure to run migrations in case there are DB schema changes by running 
`$  python manage.py makemigrations`

Dry run migrations by running following command in terminal inside backend directory
`$ python manage.py migrate --dry`

Initialise virtual env
1. Go to terminal
2. Go to backend root directory
3. run command `$ sh serve.sh dev`
4.Go to backend folder and run the command `$ serve.sh dev`

Install dependencies
1. Run command in the backend root directory `$ poetry install`


Verify python version
To print python version:
1. go to terminal
2. open the project directory
3. run following commands:
`$ python3` 
`import sys' then 'print(sys.version)'`
`exit()`

To run frontend server for development purpose:
1. go to terminal
2. open the project directory
3. run following commands:
   `cd frontend`
   `$ npm run dev`



Note:

* You might notice that the settings file is getting loaded twice on runserver command but that is just Django Auto Reload.  In development mode, Django's built-in server (run with python manage.py runserver) uses an auto-reloading feature. This means that it watches your files for changes and reloads the server when it detects any modifications. When you start the server, Django initially loads all the settings. Then, it spawns a separate thread or process to watch for file changes. This causes the settings file to be loaded again.
* You might face CORS origin issue when running Frontend and Backend server for development and the call from Frontend fails. Do not worry, this only happens during development because both servers are running on different ports. You need to disable cors middleware in Django settings.py file and then reload the Backend server to continue with development. In production, the Frontend is served from static resources either from Nginx or a CDN and this issue doesn't come up.





How to add a new module to the directory - TBA


How to add new Graphql API endpoint for your module - TBA
