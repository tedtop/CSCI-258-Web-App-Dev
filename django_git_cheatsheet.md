# Django & Git Development Cheat Sheet

## 🐍 Python Virtual Environment Setup

### Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv
# or
python3 -m venv venv
```

Note: I use the "Python: Create Environment..." magic command for creating environments

### Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Deactivate Virtual Environment
```bash
deactivate
```

Note: VSCode will automatically source a venv when it detects one in the proeject

## 📦 Django Installation & Setup

### Install Django
```bash
# Install latest Django
pip install django

# Install specific version
pip install django==4.2

# Install Black (code formatter)
pip install black
```

### Create Django Project
```bash
# Create new Django project
django-admin startproject projectname .
# or create in new directory
django-admin startproject projectname
```

### Create Django App
```bash
# Navigate to project directory first
cd projectname

# Create new app
python manage.py startapp appname
```

### Remove Migration Warnings
```bash
# Create and apply initial migrations
python manage.py makemigrations
python manage.py migrate
```

## 🚀 Django Development Commands

### Run Development Server
```bash
python manage.py runserver
# Custom port
python manage.py runserver 8080
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Make Migrations
```bash
# Create migrations for all apps
python manage.py makemigrations

# Create migrations for specific app
python manage.py makemigrations appname
```

### Apply Migrations
```bash
python manage.py migrate
```

### Django Shell
```bash
python manage.py shell
```

### Collect Static Files (Production)
```bash
python manage.py collectstatic
```

## 📋 Requirements Management

### Generate Requirements File
```bash
pip freeze > requirements.txt
```

### Install from Requirements
```bash
pip install -r requirements.txt
```

## 🔧 Code Formatting with Black

### Format Single File
```bash
black filename.py
```

### Format Entire Project
```bash
black .
```

### Check Format (Don't Apply)
```bash
black --check .
```

## 📝 Git Commands

### Initialize Repository
```bash
git init
```

### Check Status
```bash
git status
```

### Add Files
```bash
# Add all files
git add -A
# or
git add .

# Add specific file
git add filename.py
```

### Commit Changes
```bash
git commit -m "initial commit"
git commit -m "add user authentication"
```

### View Commit History
```bash
git log
git log --oneline
```

### Create Branch
```bash
git branch branchname
git checkout -b branchname  # create and switch
```

### Switch Branches
```bash
git checkout branchname
git switch branchname  # newer syntax
```

### Merge Branches
```bash
git checkout main
git merge branchname
```

### Remote Repository
```bash
# Add remote origin
git remote add origin https://github.com/username/repo.git

# Push to remote
git push origin main
git push -u origin main  # set upstream

# Pull from remote
git pull origin main
```

## 📁 Essential Django Project Structure

```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   └── migrations/
├── templates/
├── static/
├── requirements.txt
└── .gitignore
```

## 🚫 Essential .gitignore for Django

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.venv/
venv/
env/

# Django
*.log
db.sqlite3
media/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment variables
.env
```

## ⚙️ Basic Django Settings Configuration

### Add App to INSTALLED_APPS (settings.py)
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'your_app_name',  # Add your app here
]
```

### Database Configuration (settings.py)
```python
# SQLite (default)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## 🔄 Complete Workflow Example

```bash
# 1. Set up project
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install django black

# 2. Create project and app
django-admin startproject myproject .
python manage.py startapp myapp

# 3. Initial setup
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 4. Git setup
git init
git add -A
git commit -m "initial Django project setup"

# 5. Development cycle
# ... make changes ...
black .  # format code
python manage.py makemigrations
python manage.py migrate
git add -A
git commit -m "describe changes"

# 6. Run server
python manage.py runserver
```

## 🛟 Common Troubleshooting

### Virtual Environment Issues
```bash
# If activation fails, try:
python -m venv venv --clear

# Check if in virtual environment:
which python  # should show venv path
```

### Django Command Not Found
```bash
# Make sure Django is installed and venv is active
pip list | grep Django
```

### Migration Issues
```bash
# Reset migrations (be careful!)
python manage.py migrate --fake-initial
# or delete migration files and start over
```

## 📚 Useful Resources

- **Django Documentation**: https://docs.djangoproject.com/
- **Git Documentation**: https://git-scm.com/doc
- **Python Virtual Environments**: https://docs.python.org/3/tutorial/venv.html
- **Black Code Formatter**: https://black.readthedocs.io/

---

💡 **Pro Tips:**
- Always activate your virtual environment before working
- Use `git status` frequently to track changes
- Format code with Black before committing
- Create meaningful commit messages
- Keep requirements.txt updated