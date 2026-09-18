# Skill-Share-Hub

A full-stack college project for managing and showcasing student skills using FastAPI, MySQL, SQLAlchemy, HTML, CSS, and JavaScript. Second year first project(Capstone).

[![version](https://img.shields.io/badge/version-1.0.0-brightgreen)](https://github.com/jaganbprof168-source/Skill-Share-Hub/releases/tag/v1.0.0)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)


## Table of Contents

- [Description](#description)
- [Modules](#modules)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Reference](#api-reference)
- [Future Scope](#future-scope)
- [Author](#author)

## Description

This is a FastAPI application for a student skill registration and management system, built with Python.

Departments often track student skills informally, making it hard to quickly find who knows what. Skill-Share-Hub replaces that with a searchable record. Students register and post their skills through the frontend; staff can search, filter, and manage those records through a separate portal. The frontend is plain HTML/CSS/JS with no client-side framework, calling the API directly.

## Modules

- **Home Page** — dashboard with live student and skill counts.
- **Creating Profile** — student registration (roll number, name, department, year, email).
- **Posting Skills** — attach one or more skills to a roll number.
- **Portal for Officials** — search, update, delete student and skill records; look up individual profiles.

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI, Uvicorn |
| ORM | SQLAlchemy |
| Database | MySQL |
| Validation | Pydantic |
| Frontend | HTML, CSS, JavaScript |

## Project Structure

```
Skill-Share-Hub/
├── Backend/            FastAPI app, models, schemas
├── Frontend/           HTML pages, shared stylesheet, scripts
├── Docs/               Capstone documentation
├── .gitignore
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/jaganbprof168-source/Skill-Share-Hub.git
cd Skill-Share-Hub
python -m venv venv
source venv/bin/activate     # venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Database Setup

```sql
CREATE DATABASE skillshare_hub;
```

Set the connection string in the backend config:

```python
DATABASE_URL = "mysql+pymysql://username:password@localhost/skillshare_hub"
```

Tables (created automatically on first run):

- **Students_info** — `rollno` (PK), `Name`, `Department`, `Year`, `Email`, `Skill`
- **Skill_Sets** — `rollno` (FK), `Skill`

## Running the Application

```bash
cd Backend
uvicorn End:app --reload
```

Runs at `http://127.0.0.1:8000`; interactive docs at `/docs`. Open the frontend pages from `Frontend/` in a browser once the server is running.

## API Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/StudentsDetails` | Register a new student |
| `GET` | `/Allstudentinfo` | List all students |
| `GET` | `/parstudentinfo/{id}` | Fetch a student by roll number |
| `PUT` | `/Update/{id}` | Update a student |
| `DELETE` | `/DeleteStudentsinfo/{id}` | Remove a student and their skill entry |
| `POST` | `/Skills` | Add a skill |
| `GET` | `/Skillstudentinfo`
