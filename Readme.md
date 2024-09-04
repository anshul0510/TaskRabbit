TaskRabbit Project
This project is a task management application built with Django. It allows users to create, update, delete, and view tasks, along with basic user account management features.

Features
User Authentication
User registration
User login
User logout
Profile management

Task Management
Create tasks
List tasks
Update tasks
Delete tasks
Image Upload
Upload user images

Installation

Clone the Repository
git clone https://github.com/yourusername/taskrabbit.git
cd taskrabbit

Create a Virtual Environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

Install Dependencies
pip install -r requirements.txt

Apply Migrations
python manage.py migrate

Create a Superuser (Optional)
python manage.py createsuperuser

Run the Development Server
python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000 to see the application in action.
API Endpoints
User Authentication

Register User
POST /register/
Data: username, email, password, password2

Login User
POST /login/
Data: username, password

Logout User
GET /logout/
Task Management

List Tasks
GET /tasks/

Create Task
GET /tasks/create/ (Form to create a new task)
POST /tasks/create/ (Submit new task data)

Update Task
GET /tasks/update/<pk>/ (Form to update an existing task)
POST /tasks/update/<pk>/ (Submit updated task data)

Delete Task
GET /tasks/delete/<pk>/ (Confirmation page)
POST /tasks/delete/<pk>/ (Submit task deletion)
Image Upload
Upload Image
GET /upload/ (Form to upload an image)
POST /upload/ (Submit image data)
User Profile
Update Profile
GET /profile/ (Form to update user profile)
POST /profile/ (Submit profile data)
Directory Structure
project_root/
manage.py - Django management script
taskrabbit/ - Project directory
settings.py - Django settings
urls.py - URL configurations
wsgi.py - WSGI entry point
users/ - User-related models and views
models.py - UserProfile model
views.py - User-related views
forms.py - User-related forms
urls.py - User-related URL patterns
tasks/ - Task-related models and views
models.py - Task model
views.py - Task-related views
forms.py - Task-related forms
urls.py - Task-related URL patterns

