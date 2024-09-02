# Use the official Python image from the Docker Hub
FROM python:3.10.14 AS requirements

# Set work directory
WORKDIR /src

# Install Poetry
RUN pip install poetry

COPY backend/pyproject.toml backend/poetry.lock ./
RUN poetry export -f requirements.txt --without-hashes -o /src/requirements.txt

FROM node:20.10.0 AS frontend

# Set the working directory:
WORKDIR /app

# Copy package.json and package-lock.json
COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY frontend .

RUN npm run build

# Use the official Python image from the Docker Hub
FROM python:3.10.14

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install requirements
COPY --from=requirements /src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of your project code
COPY backend .

# Copy dist folder
COPY --from=frontend /app/dist ./main/static/dist

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Specify the command to run your application - TO BE FIXED on how to run two commands in one line
#CMD [ "python", "manage.py", "migrate", "&&", "gunicorn", "--bind", "0.0.0.0:8000", "main.wsgi:application"]
