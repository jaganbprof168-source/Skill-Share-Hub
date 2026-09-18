# Skill-Share-Hub

A FastAPI-based backend and frontend for a student skill registration and lookup system, built as a college capstone project.

![version](https://img.shields.io/badge/version-1.0-blue) ![license](https://img.shields.io/badge/license-MIT-green)

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
