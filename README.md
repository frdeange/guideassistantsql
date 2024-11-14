# SQL Virtual Assistant

This project is a virtual assistant that helps generate and execute SQL queries on a SQL Server database. The project is divided into two parts: a backend developed with FastAPI and a frontend developed with Flask.

## Project Structure


## Development Environment Setup

This project uses development containers to facilitate the setup of the environment. Make sure you have Docker and Docker Compose installed on your machine.

1. Clone the repository:
    ```sh
    git clone <REPOSITORY_URL>
    cd <REPOSITORY_NAME>
    ```

2. Open the project in Visual Studio Code.

3. Open the command palette (Ctrl+Shift+P) and select `Remote-Containers: Reopen in Container`.

4. Once the container is ready, dependencies will be automatically installed, and the database will be initialized.

## Backend

The backend is developed with FastAPI and is located in the `backend/app` directory.

### Endpoints

- `POST /procesar_consulta/`: Processes a query sent by the user and returns the results of the SQL query.

### Dependencies

The backend dependencies are listed in `backend/requirements.txt`.

## Frontend

The frontend is developed with Flask and is located in the `frontend/app` directory.

### Routes

- `/`: Main page where the user can enter their query.

### Dependencies

The frontend dependencies are listed in `frontend/requirements.txt`.

## Database

The database initialization script is located in `database/init_db.sql`. This script creates the `Clientes` and `Pedidos` tables and populates them with sample data.

## Environment Variables

Make sure to configure the following environment variables in the corresponding `.env` files:

- `SQLSERVER_HOST`
- `SQLSERVER_PORT`
- `SQLSERVER_USER`
- `SQLSERVER_PASSWORD`
- `OPENAI_API_KEY`
- `BACKEND_URL`

## Running the Project

To run the project, make sure the development container is running and access the frontend URL in your browser (by default, `http://localhost:5000`).

## Contributing

If you want to contribute to this project, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.