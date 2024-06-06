# Crypto Price API

This project is a RESTful API for retrieving and managing cryptocurrency price data. It allows users to get real-time price information from the KuCoin exchange, save this data to a PostgreSQL database, and retrieve historical price records.

## Dependencies

This project relies on the following dependencies:

- [Poetry](https://python-poetry.org/): A dependency manager for Python projects. Install it to manage project dependencies and virtual environments.
- [Docker](https://www.docker.com/): A containerization platform that allows you to package and distribute applications and their dependencies as containers.

Ensure that both Poetry and Docker are installed on your system before proceeding with the setup and usage of this project.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone git clone https://github.com/kennedybacelar/qorpo-crypto-api.git

2. Navigate to the project directory:

    ```bash
    cd qorpo-crypto-api
    
3. Install dependencies using Poetry:

    ```bash
    poetry install

## Usage

### Running the API

You can run the API in multiple ways:

1. Using Gunicorn:

    ```bash
    gunicorn -c gunicorn_config.py app.main:create_app()

2. As a Python Module:

    ```bash
    python -m run

3. Using Docker:

    ```bash
    docker-compose up


### Running Tests With Docker
To make running tests easier and more convenient, it's recommended to utilize Docker
If you're using Docker, you can run tests using the following command:

    ```bash
    docker compose up -d
    poetry run pytest -s -v
    ```

### Running Tests Without Docker

However, if someone prefers to run the application and tests directly on their host machine without Docker, they'll need to set up the databases accordingly. Here's how they can configure the databases:

1. **Database Setup for Application**:
   - PostgreSQL database with:
     - **Database Name**: qorpo_database_sample
     - **Username**: username
     - **Password**: password
     - **Host**: localhost (or host IP)
     - **Port**: 5432

2. **Database Setup for Tests**:
   - PostgreSQL database with:
     - **Database Name**: qorpo_database_test
     - **Username**: username
     - **Password**: password
     - **Host**: localhost (or host IP)
     - **Port**: 5433 (to avoid port conflict)

3. **Initializing Databases**:
   - Run `00_init.sql` against both databases to initialize schema and data.

Ensure databases are correctly configured and initialized on your host machine.

```bash
    poetry run pytest -s -v
```


## Endpoints

The API provides the following endpoints:

1. **GET /price/{currency}**: Get the last bid price from the KuCoin exchange for the specified cryptocurrency paired with USDT.

2. **GET /price/history?page={page}**: Retrieve paginated historical price records from the database (page size is 10).

3. **DELETE /price/history**: Delete all historical price records from the database.


## Contributing

Author: Kennedy Bacelar
