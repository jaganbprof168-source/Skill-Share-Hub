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
