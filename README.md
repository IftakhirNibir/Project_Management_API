# Project Management API

## Overview

The Project Management API facilitates team collaboration on projects by providing a comprehensive set of endpoints to manage users, projects, tasks, and comments. Designed for integration with both front-end web and mobile applications, this API serves as the backbone for a robust project management tool.

## Features

- **User Management**: Create, authenticate, update, and delete user accounts.
- **Project Management**: Manage projects, including creation, retrieval, updating, and deletion of project details.
- **Task Management**: Organize tasks within projects, assign tasks to users, and update task statuses.
- **Comment Management**: Add, retrieve, update, and delete comments on tasks to facilitate team communication.

## Setup Instructions
1. First, you need to install Python and pip on your local machine
2. Create a folder and open the terminal in that folder
3. Create a virtual environment using the terminal. For example, the environment name is "env"
```bash
python -m venv env 
```
4. Activate the environment
```bash
env\Scripts\activate
```
5. Now you need to clone the repository.
```sh
git clone https://github.com/IftakhirNibir/Project_Management_API.git
```
6. Open the project folder
```sh
cd Project_Management_API
```
6. Install the required prerequisites using
```sh
pip install -r requirement.txt
```
7. Open "Project_Management" folder
```sh
cd Project_Management
```
8. Now run the server
```sh
py manage.py runserver
```
9. Copy the link and add endpoints for testing API using Postman
```sh
http://127.0.0.1:8000/
```

## Endpoints

### Users
- Register User: `POST /api/users/register/`
- Login User: `POST /api/users/login/`
- Get User Details: `GET /api/users/{id}/`
- Update User: `PUT/ /api/users/{id}/`
- Delete User: `DELETE /api/users/{id}/`

### Projects
- List Projects: `GET /api/projects/`
- Create Project: `POST /api/projects/`
- Retrieve Project: `GET /api/projects/{id}/`
- Update Project: `PUT /api/projects/{id}/`
- Delete Project: `DELETE /api/projects/{id}/`

### Tasks
- List Tasks: `GET /api/projects/{project_id}/tasks/`
- Create Task: `POST /api/projects/{project_id}/tasks/`
- Retrieve Task: `GET /api/tasks/{id}/`
- Update Task: `PUT /api/tasks/{id}/`
- Delete Task: `DELETE /api/tasks/{id}/`

### Comments
- List Comments: `GET /api/tasks/{task_id}/comments/`
- Create Comment: `POST /api/tasks/{task_id}/comments/`
- Retrieve Comment: `GET /api/comments/{id}/`
- Update Comment: `PUT /api/comments/{id}/`
- Delete Comment: `DELETE /api/comments/{id}/`

## API Documentation
You can view the API documentation at 
```sh
http://127.0.0.1:8000/swagger/
```
## Contributing
Contributions are welcome! Please create a pull request or submit an issue for any improvements or bug fixes.
