# Web Application Development Project

Welcome to our collaborative Web Application Development project! This repository contains Django web applications and Python networking examples for our coursework.

## Getting Started

Follow these step-by-step instructions to set up the project on your local machine.

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/tedtop/CSCI-258-Web-App-Dev
cd CSCI-258-Web-App-Dev
```

### 2. Create Python Virtual Environment

You have two options for creating your virtual environment:

#### Option A: Using VSCode (Recommended)

1. Open the project folder in VSCode
2. Open the Command Palette (`Cmd+Shift+P` on Mac, `Ctrl+Shift+P` on Windows/Linux)
3. Type "Python: Create Environment..." and select it
4. Choose "Venv" as your environment type
5. Select your Python interpreter (preferably Python 3.8 or higher)
6. VSCode will automatically:
   - Create a `.venv` folder in your project
   - Detect and activate the virtual environment
   - Source the environment automatically in VSCode's integrated terminal

**Note**: When using VSCode, the integrated terminal will automatically source `.venv/bin/activate` (on Mac/Linux) or `.venv\Scripts\Activate.ps1` (on Windows). However, if you use other terminals outside of VSCode, you'll need to manually activate the environment using the instructions in Option B.

#### Option B: Command Line Setup

Create the virtual environment manually:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**On Mac/Linux:**
```bash
source .venv/bin/activate
```

**On Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

You should see `(.venv)` at the beginning of your command prompt when the environment is active.

### 4. Install Requirements

Install all required Python packages:

```bash
python -m pip install -r requirements.txt
```

This will install:
- Django 5.0.14
- All necessary dependencies

### 5. Initial Django Setup (if needed)

If working with the Django project, you may need to run migrations:

```bash
cd django_project
python manage.py migrate
```

## Working with the Repository

### Getting Latest Changes

Before starting work, always pull the latest changes:

```bash
git pull origin main
```

Or, the shortcut

```bash
git pull
```

### Making Changes

#### 1. Create a New Branch

**Important**: Always create a new branch for your changes. Never work directly on the main branch.

```bash
git checkout -b your-name-feature-description
```

Example:
```bash
git checkout -b john-client-server-improvements
```

#### 2. Make Your Changes

- Edit files as needed
- Test your changes
- Create your personal README file (e.g., `JohnReadme.md`) with information about yourself

#### 3. Add and Commit Your Changes

Stage your changes:
```bash
git add .
```

Or add specific files:
```bash
git add filename.py
git add JohnReadme.md
```

Commit with a descriptive message:
```bash
git commit -m "Add personal README and improve client error handling"
```

#### 4. Push Your Branch

Push your branch to the remote repository:
```bash
git push origin your-branch-name
```

Example:
```bash
git push origin john-client-server-improvements
```

#### 5. Create a Pull Request

1. Go to the GitHub repository in your web browser
2. You should see a banner suggesting to create a pull request for your recently pushed branch
3. Click "Compare & pull request"
4. Fill in the title and description of your changes
5. Click "Create pull request"

Alternatively:
1. Go to the repository on GitHub
2. Click on "Pull requests" tab
3. Click "New pull request"
4. Select your branch from the "compare" dropdown
5. Add title and description
6. Click "Create pull request"

## Running the Applications

### Django Web Application

1. Navigate to the django_project directory:
   ```bash
   cd django_project
   ```

2. Run the development server:
   ```bash
   python manage.py runserver
   ```

3. Open your browser to `http://127.0.0.1:8000`

## Troubleshooting

### Virtual Environment Issues

- **Environment not activating**: Make sure you're in the correct directory and using the right activation script for your operating system
- **"python not found"**: Try using `python3` instead of `python`
- **Permission errors on Windows**: Run PowerShell as administrator or change execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### Git Issues

- **"Permission denied"**: Make sure you have write access to the repository
- **Merge conflicts**: Contact the project maintainer for help resolving conflicts
- **Branch not found**: Make sure you've pushed your branch: `git push origin your-branch-name`

## Best Practices

1. **Always work in a virtual environment**
2. **Create descriptive branch names**: `your-name-feature-description`
3. **Write meaningful commit messages**: Describe what you changed and why
4. **Test your changes** before committing
5. **Pull latest changes** before starting new work
6. **Keep commits small and focused**: One feature/fix per commit when possible

## Assignment Reminder

- Clone the repository (don't fork)
- Create your virtual environment
- Install requirements
- Create a new branch
- Create your personal README file (e.g., `YourNameReadme.md`)
- Add information about yourself
- Commit and push your branch
- Create a pull request

Happy coding! 🚀