## Description
Task Manager is a Django-based web application for managing tasks.
It supports users, task statuses, labels, and task assignment, with basic access rules and deletion protections.

[![Actions Status](https://github.com/Cur1yB/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Cur1yB/python-project-52/actions)
## Deploy

[Click me🥵](https://python-project-52-w5q1.onrender.com)


## Features
- User registration and authentication
- Create/read/update/delete (CRUD) for:
  - statuses
  - labels
  - tasks
- Assign an executor to a task
- Task filtering
- Deletion protection for related objects (you can’t delete an entity if it is used)
- Access rules (e.g., only the author can delete a task)

## Requirements
- Python 3.10+ (recommended)
- Make
- Git
- (Optional) PostgreSQL for production-like setup; SQLite can be used locally if the project is configured for it

## Installation & Setup (local)
Clone the repository:
```bash
git clone https://github.com/Cur1yB/python-project-52.git
cd python-project-52
```

Install dependencies:
```bash
make install
```

Apply migrations:
```bash
make migrate
```

Run the development server:
```bash
make dev
```

Open in your browser:
- http://127.0.0.1:8000

## Environment variables
The project uses environment variables for configuration.  
Create a `.env` file in the project root (if your Makefile/project expects it) and set values such as:

```bash
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=127.0.0.1,localhost
```

> Note: exact variable names may differ depending on your settings module.  
If you share your `.env.example` (or settings), I can adjust this section precisely.

## Useful Make commands
Typical commands (may vary depending on the Makefile):
```bash
make install   # install dependencies
make migrate   # apply migrations
make run       # run dev server
make test      # run tests
make lint      # run linters (if configured)
```

## License
MIT (or specify your license here).
``````markdown
[![Actions Status](https://github.com/Cur1yB/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Cur1yB/python-project-52/actions)

## Deploy
https://python-project-52-w5q1.onrender.com

## Description
Task Manager is a Django-based web application for managing tasks.
It supports users, task statuses, labels, and task assignment, with basic access rules and deletion protections.

## Features
- User registration and authentication
- Create/read/update/delete (CRUD) for:
  - statuses
  - labels
  - tasks
- Assign an executor to a task
- Task filtering
- Deletion protection for related objects (you can’t delete an entity if it is used)
- Access rules (e.g., only the author can delete a task)

## Requirements
- Python 3.10+ (recommended)
- Make
- Git
- (Optional) PostgreSQL for production-like setup; SQLite can be used locally if the project is configured for it

## Installation & Setup (local)
Clone the repository:
```bash
git clone https://github.com/Cur1yB/python-project-52.git
cd python-project-52
```

Install dependencies:
```bash
make install
```

Apply migrations:
```bash
make migrate
```

Run the development server:
```bash
make run
```

Open in your browser:
- http://127.0.0.1:8000

## Environment variables
The project uses environment variables for configuration.  
Create a `.env` file in the project root (if your Makefile/project expects it) and set values such as:

```bash
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=127.0.0.1,localhost
```

> Note: exact variable names may differ depending on your settings module.  
If you share your `.env.example` (or settings), I can adjust this section precisely.

## Useful Make commands
Typical commands (may vary depending on the Makefile):
```bash
make install   # install dependencies
make migrate   # apply migrations
make run       # run dev server
make test      # run tests
make lint      # run linters (if configured)
```

## License
MIT (or specify your license here).
```