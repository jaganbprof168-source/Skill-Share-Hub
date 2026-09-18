SkillShare Hub

A full-stack college project for managing and showcasing student skills using FastAPI, MySQL, SQLAlchemy, HTML, CSS, and JavaScript.




Table of Contents

Description

Modules

Tech Stack

Project Structure

Installation

Database Setup

Running the Application

API Reference

Documentation

Future Scope

License

Author

Description

SkillShare Hub is a full-stack web application developed to organize and manage student skill information in a college environment.

The system provides a centralized platform where student profiles can be registered and their skills can be recorded. The application also provides a separate portal for officials to view, search, update, and manage student and skill information.

The frontend is developed using HTML, CSS, and JavaScript. It communicates with the backend through REST API requests. The backend is developed using Python and FastAPI, while SQLAlchemy is used to communicate with the MySQL database.

Modules

1. Home Page

The Home Page provides the main interface of SkillShare Hub and gives access to the major features of the application.

2. Creating Profile

The Creating Profile module allows student information to be registered in the system. The profile includes:

Roll Number

Name

Department

Year

Email

Skill

3. Posting Skills

The Posting Skills module allows a skill to be associated with a student's roll number. The skill information is stored separately in the Skill_Sets table and is linked to the student record through a foreign key.

4. Portal for Officials

The Portal for Officials provides management features for student and skill information. Officials can:

View student records

View skill records

Search for a skill

View an individual student profile

Update student information

Update skill information

Delete student records

Tech Stack

Layer

Technology

Programming Language

Python

Backend Framework

FastAPI

Server

Uvicorn

ORM

SQLAlchemy

Database

MySQL

Data Validation

Pydantic

Frontend

HTML, CSS, JavaScript

Project Structure

Skill-Share-Hub/
├── Backend/
│   ├── DataBase.py
│   ├── End.py
│   ├── Execution.py
│   ├── Model.py
│   └── Table.py
│
├── Docs/
│   ├── SkillShare_Hub_Project_Documentation.docx
│   ├── SkillShare_Hub_Project_Documentation.pdf
│   └── ScreenShots/
│
├── Frontend/
│   ├── index.html
│   ├── register.html
│   ├── manage-students.html
│   ├── add-skill.html
│   ├── manage-skills.html
│   ├── student-profile.html
│   └── style.css
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

Installation

1. Clone the repository

git clone https://github.com/jaganbprof168-source/Skill-Share-Hub.git
cd Skill-Share-Hub

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

Windows:

venv\Scripts\activate

Linux / macOS:

source venv/bin/activate

4. Install the required packages

pip install -r requirements.txt

Database Setup

SkillShare Hub uses MySQL as its relational database.

Create the database using:

CREATE DATABASE project;

The application uses the following main tables:

Students_info

Stores the main student information.

rollno - Primary Key

Name

Department

Year

Email

Skill

Skill_Sets

Stores skill information associated with students.

rollno - Primary Key and Foreign Key

Skill

The database connection is configured using the DATABASE_URL environment variable.

Create a .env file in the project root:

DATABASE_URL=mysql+pymysql://USERNAME:PASSWORD@localhost:3306/project

Replace USERNAME and PASSWORD with your own MySQL credentials.

Do not upload the .env file to GitHub. It is already included in .gitignore.

Running the Application

Open a terminal in the Backend folder:

cd Backend

Start the FastAPI application using:

uvicorn End:app --reload

The backend will run locally at:

http://127.0.0.1:8000

FastAPI's interactive API documentation is available at:

http://127.0.0.1:8000/docs

After starting the backend, open the required HTML page from the Frontend folder in a browser.

API Reference

Student APIs

Method

Endpoint

Description

POST

/StudentsDetails

Register a student

GET

/Allstudentinfo

Retrieve all student records

GET

/parstudentinfo/{id}

Retrieve a student by roll number

PUT

/Update/{id}

Update student information

DELETE

/DeleteStudentsinfo/{id}

Delete a student and linked skill record

Skill APIs

Method

Endpoint

Description

POST

/Skills

Add a skill

GET

/Skillstudentinfo

Retrieve all skill records

GET

/Skillstudentinfo/{ques}

Search skill records

PUT

/UpdateSkill/{id}

Update a skill record

Documentation

Detailed information about the project, including system study, proposed work, tools used, modules, database design, testing, screenshots, conclusion, and future enhancements is available in the Docs folder.

The project documentation is provided in both Word and PDF formats.

Future Scope

The following features can be considered for future versions of SkillShare Hub:

Authentication and role-based access for students and officials

Support for multiple skills and proficiency levels

Advanced search and filtering

Pagination for larger student records

CSV export of student and skill information

Cloud deployment

Improved security and access control

License

This project is licensed under the MIT License.

You are free to use, copy, modify, and distribute the code, subject to the terms of the MIT License. See the LICENSE file for the complete license text.

Author

Jagan B

BSc Information Technology
Sri Krishna Arts and Science College, Coimbatore

SkillShare Hub v1.0.0
