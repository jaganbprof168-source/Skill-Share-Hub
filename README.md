A SYSTEM FOR STUDENT SKILL MANAGEMENT
___________________________________________________
A full-stack college project for managing and showcasing student skills using FastAPI, MySQL, SQLAlchemy, HTML, CSS, and JavaScript. Second year first project(Capstone).

[![version](https://img.shields.io/badge/version-1.0.0-brightgreen)](https://github.com/jaganbprof168-source/Skill-Share-Hub/releases/tag/v1.0.0)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

Table of Contents
_________________________________________________________
•	Description

•	Modules

•	Tech Stack

•	Project Structure

•	Installation

•	Database Setup

•	Running the Application

•	API Reference

•	Documentation

•	Future Scope

•	License

•	Author


Description

_________________________________________________________
SkillShare Hub is a full-stack web application developed to organize and manage student skill information in a college environment.
The system provides a centralized platform where student profiles can be registered and their skills can be recorded. The application also provides a separate portal for officials to view, search, update, and manage student and skill information.
The frontend is developed using HTML, CSS, and JavaScript. It communicates with the backend through REST API requests. The backend is developed using Python and 
FastAPI, while SQLAlchemy is used to communicate with the MySQL database.



Modules
_________________________________________________________
1. Home Page
The Home Page provides the main interface of SkillShare Hub and gives access to the major features of the application.

3. Creating Profile
The Creating Profile module allows student information to be registered in the system. The profile includes:
•	Roll Number
•	Name
•	Department
•	Year
•	Email
•	Skill

5. Posting Skills
The Posting Skills module allows a skill to be associated with a student's roll number. The skill information is stored separately in the Skill_Sets table and is linked to the student record through a foreign key.

7. Portal for Officials
The Portal for Officials provides management features for student and skill information. Officials can:
•	View student records
•	View skill records
•	Search for a skill
•	View an individual student profile
•	Update student information
•	Update skill information
•	Delete student records

