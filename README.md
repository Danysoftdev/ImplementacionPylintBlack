# TALLER IMPLEMENTACIÓN PYLINT Y BLACK

## FastAPI Application

This project is a FastAPI-based application that provides endpoints to manage categories and other resources.

## Prerequisites

Make sure you have the following software installed:

- [Docker](https://www.docker.com/)
- [Python 3.8+](https://www.python.org/downloads/)

## Initial Setup

1. Clone the repository:
    ```bash
    git clone <https://github.com/Danysoftdev/ImplementacionPylintBlack.git>
    cd <https://github.com/Danysoftdev/ImplementacionPylintBlack.git>
    ```

2. Install the Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create and complete the .env file:
    ```bash
    cp .env.example .env
    ```

    Then edit the .env file to provide the appropriate values, such as database credentials.

## Starting the Database with Docker

To start the database using Docker, follow these steps:

1. Before running the containers, make sure to build them using the following command from the project root:

    ```bash
    docker-compose build
    ```

2. Run the following command:
    ```bash
    docker-compose up -d
    ```

This command will start the containers defined in the `docker-compose.yml` file, including the database configured for your project. The `-d` option runs the containers in the background.

3. To verify that the containers are running, use:
    ```bash
    docker ps
    ```

## Running the Application

1. Access the interactive API documentation at:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Analyzing the Code with Pylint

To analyze the code using Pylint, follow these steps:

1. Install Pylint if you haven't already:
    ```bash
    pip install pylint
    ```

2. Run Pylint using the provided configuration file:
    ```bash
    pylint --rcfile=pylint.yml <path to the file or directory you want to analyze>
    ```

For example, to analyze the entire project:
   ```bash
   pylint --rcfile=pylint.yml .
   ```
## Shutting Down the Database and Application

1. To stop the Docker containers, use:
    ```bash
    docker-compose down
    ```
2. To stop the FastAPI application, press Ctrl + C in the terminal where uvicorn is running.
