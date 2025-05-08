# Todo App

A simple todo application built with Django.

## Features

- Create, read, update, and delete todo items
- Mark todos as complete/incomplete
- Filter todos by status
- User authentication

## Installation

### Option 1: Local Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AhmedHamdy85/todos
    cd todos
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Access the app at http://localhost:8000

### Option 2: Docker Installation

1. Pull the Docker image:
    ```bash
    docker pull ahramadan/todo
    ```

2. Run the container:
    ```bash
    docker run -p 8000:8000 ahramadan/todo
    ```

3. Access the app at http://localhost:8000

## Usage

1. Register a new account or login
2. Add new todos by clicking the "Add Todo" button
3. Mark todos as complete by checking the checkbox
4. Edit or delete todos using the respective buttons
5. Filter todos using the filter options

## API Endpoints

### Tasks Endpoints
- `GET /tasks/` - List all tasks
- `POST /tasks/create/` - Create a new task
- `GET /tasks/{id}/` - Retrieve a specific task
- `PUT /tasks/update/{id}/` - Update a task
- `DELETE /tasks/delete/{id}/` - Delete a task
- `POST /tasks/switch/{id}/` - Toggle task completion status

### User Endpoints
- `POST /user/regester/` - Register a new user
- `POST /user/login/` - Login and obtain authentication token
- `GET /user/` - List users
- `GET /user/{id}` - Retrieve a specific user
- `POST /user/logout/` - Logout user

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request
