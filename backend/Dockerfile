# Use the official Python image from the Docker Hub
FROM python:3.10.14

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only the necessary files for faster builds
COPY pyproject.toml poetry.lock ./

# Install dependencies (without dev dependencies)
RUN poetry install --no-root --no-dev

# Copy the rest of your project code
COPY . .

# Run migrations and collect static files
#RUN python manage.py migrate
#RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Specify the command to run your application
CMD ["python", "manage.py", "runserver", "--settings=main.settings.dev"]
