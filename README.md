# Project AGENT-BOURNE
An agent which can get your tasks done. Your personal assistant.

The backend uses Python version 3.12.2 

###To run backend server:

####Make sure to setup and run Postgres DB on localhost:
1. Install Postgres DB
2. Install Postgres client
3. Create a DB with name 'agent_bourne'
4. Create username and password

To do the above steps run the following commands in terminal after installing Postgres:
- `$ psql`
- `CREATE DATABASE <db_role>;`
- `CREATE USER <db_role> WITH PASSWORD 'your-password';`
- `GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <db_role>;`
- `\c <db_name>`
- `GRANT ALL PRIVILEGES ON SCHEMA public TO <db_role>;`
- `ALTER DATABASE <db_name> OWNER TO <db_role>;`
- `$ \q`

#### Create .env file in the root folder `backend/.env`
1. Go to terminal
2. go to backend dir `cd Project-Agent-Bourne/backend`
3. `vim .env`
4. copy keys from `sample.env` to `.env` and update the values of the keys


#### Initialise virtual env for Backend app. 
We use poetry for package management and installation
1. Go to terminal
2. go to backend dir `cd Project-Agent-Bourne/backend`
3. install and setup poetry using https://python-poetry.org/docs/
4. run command `$ sh serve.sh dev`

#### Make sure to create migrations for DB changes
1. Go to terminal
2. go to backend dir `cd Project-Agent-Bourne/backend`
3. Make sure to run migrations in case there are DB schema changes by running 
`$  python manage.py makemigrations`

#### Dry run migrations by running following command in terminal inside backend directory
`$ python manage.py migrate --dry`

#### Running the Backend App
1. Go to terminal
2. go to backend dir `cd Project-Agent-Bourne/backend`
3. run command `poetry run python manage.py runserver --settings=main.settings.dev` (you can use different values like main.settings.prod and main.settings.test for Production and Test Env respectively.) 


#### Verifying your current python version
To print python version:
1. Go to terminal
2. go to backend dir `cd Project-Agent-Bourne/backend`
3. run following commands:
   1. `$ python3`
   2. `import sys' then 'print(sys.version)'`
   3. `exit()`

#### To run frontend server for development purpose:
1. Go to terminal
2. go to backend dir `cd Project-Agent-Bourne/frontend`
3. run following commands:
   1. `cd frontend`
   2. `npm install`
   3. `npm run dev`


#### Generating dist folder for frontend static assets

Note:

* You might notice that the settings file is getting loaded twice on runserver command but that is just Django Auto Reload.  In development mode, Django's built-in server (run with python manage.py runserver) uses an auto-reloading feature. This means that it watches your files for changes and reloads the server when it detects any modifications. When you start the server, Django initially loads all the settings. Then, it spawns a separate thread or process to watch for file changes. This causes the settings file to be loaded again.
* You might face CORS origin issue when running Frontend and Backend server for development and the call from Frontend fails. Do not worry, this only happens during development because both servers are running on different ports. You need to disable cors middleware in Django settings.py file and then reload the Backend server to continue with development. In production, the Frontend is served from static resources either from Nginx or a CDN and this issue doesn't come up.





How to add a new module to the directory - TBA


How to add new Graphql API endpoint for your module - TBA
