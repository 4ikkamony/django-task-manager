# Task Manager

## About The Project

This Django-powered app is here to help people manage their never-ending to-dos. It lets you create and assign tasks, and track their completion. Also, I did my best to keep the user's self-esteem high - one can always visit his profile and see all the tasks he had ever done. Magnificent

### Features
- **CRUD operations** for Tasks, Workers, and TaskTypes
- **Assign/Unassign** Workers to Tasks
- **Change Task Status** (Completed/Not Completed)
- **Search** TaskTypes, Workers, and Tasks
- **Admire** Completed and Not Completed Tasks for each Worker

## [Project deployed on Render](https://django-task-manager-zyxj.onrender.com/)
login:
```
user
```
password:
```
user1234
```

## Getting Started

Follow these steps to set up the project locally.

### Prerequisites

- Python (>=3.10)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/4ikkamony/django-task-manager.git
   cd django-task-manager
   ```
2. Set up a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Linux/MacOS use `source venv/bin/activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements-dev.txt
   ```
4. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser for admin access:
   ```sh
   python manage.py createsuperuser
   ```
   Or load fixture with some pre-made entries:
    ```sh
    python manage.py loaddata task_manager_data.json
    ```
   and use <strong>admin.user</strong> <strong>1qazcde3</strong> to login
6. Run the development server:
   ```sh
   python manage.py runserver
   ```
You can also create your own .env file based on .env.sample
```sh
cp .env.sample .env
```
And set your own environmental variables, such as:
  - your postgresql connection data
  - django secret key, path to settings module and hostname
  - credentials for task_manager.management.commands.add_admin_user command
## Usage

- Log in to create and manage tasks.
- Assign workers to tasks and update statuses as needed.
- Search for specific tasks, task types, or workers.
- View completed and ongoing tasks per worker.

## Even to do list app needs it's own TODO:

- [ ] Add filters for Task and Worker lists: to help look for relevant tasks
- [ ] Add support for Teams, to help group Workers and make management a bit easier
- [ ] Add support for Projects, groups of tasks, to make managing long-term tasks possible
- [ ] Display history: who assigned who and who completed what
- [ ] Extend search functionality

## Templates and styles used: [Soft-UI Design by Creative Tim](https://github.com/app-generator/django-soft-ui-design)

