A SYSTEM FOR STUDENT SKILL MANAGEMENT
___________________________________________________
A full-stack college project for managing and showcasing student skills using FastAPI, MySQL, SQLAlchemy, HTML, CSS, and JavaScript. Second year first project(Capstone).

[![version](https://img.shields.io/badge/version-1.0.0-brightgreen)](https://github.com/jaganbprof168-source/Skill-Share-Hub/releases/tag/v1.0.0)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)


Table of Contents

Description

Modules

Tech Stack

Project Structure

Installation

Database Setup

Running the Application

API Reference

Future Scope

Author

Description

This is a FastAPI application for a student skill registration and management system, built with Python.

Departments often track student skills informally, making it hard to quickly find who knows what. Skill-Share-Hub replaces that with a searchable record. Students register and post their skills through the frontend; staff can search, filter, and manage those records through a separate portal. The frontend is plain HTML/CSS/JS with no client-side framework, calling the API directly.

Modules

Home Page — dashboard with live student and skill counts.
Creating Profile — student registration (roll number, name, department, year, email).

Posting Skills — attach one or more skills to a roll number.
Portal for Officials — search, update, delete student and skill records; look up individual profiles.

Tech Stack

Layer	Technology

Backend	FastAPI, Uvicorn

ORM	SQLAlchemy

Database	MySQL

Validation	Pydantic

Frontend	HTML, CSS, JavaScript

Project Structure

Skill-Share-Hub/

├── Backend/            FastAPI app, models, schemas

├── Frontend/           HTML pages, shared stylesheet, scripts

├── Docs/               Capstone documentation

├── .gitignore

└── requirements.txt

Installation

bash

git clone https://github.com/jaganbprof168-source/Skill-Share-Hub.git

cd Skill-Share-Hub

python -m venv venv

source venv/bin/activate     # venv\Scripts\activate on Windows

pip install -r requirements.txt

Database Setup

sql

CREATE DATABASE skillshare_hub;

Set the connection string in the backend config:

python

DATABASE_URL = "mysql+pymysql://username:password@localhost/skillshare_hub"

Tables (created automatically on first run):

Students_info — rollno (PK), Name, Department, Year, Email, Skill

Skill_Sets — rollno (FK), Skill

Running the Application

bash

uvicorn main:app --reload

Runs at http://127.0.0.1:8000; interactive docs at /docs. Open the frontend pages from Frontend/ in a browser once the server is running.

API Reference

Method	Endpoint	Description

POST	/students	Register a new student

GET	/students	List all students

GET	/students/{rollno}	Fetch a student

PUT	/students/{rollno}	Update a student

DELETE	/students/{rollno}	Remove a student

POST	/skills	Add a skill

GET	/skills	List all skills

GET	/skills/search/{keyword}	Search skills by keyword

PUT	/skills/{rollno}	Update a skill entry

DELETE	/skills/{rollno}	Remove a skill entry

Future Scope

Authentication for the Portal for Officials

Skill endorsements verified by faculty

CSV export of filtered results

Hosted deployment

License


This project is licensed under the MIT License — you are free to use, copy, modify, and distribute this code, provided the original copyright notice is retained.

Author

Jagan B BSc Information Technology, Sri Krishna Arts and Science College, Coimbatore
