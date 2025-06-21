# 🦸‍♂️ Flask Hero Management App

This is a simple Flask application that allows you to manage superheroes, their powers, and the strength of their abilities. It uses **Flask**, **SQLAlchemy**, and **SQLite** to create and manage relational data between heroes and powers.

---

## Features

- Add and manage superheroes
- Add and manage powers
- Assign powers to heroes with strength levels
- Edit or delete heroes, powers, and assignments
- User-friendly web interface with structured forms and tables

---

## Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Database**: SQLite
- **Frontend**: HTML (Jinja2 templating)

---

## Project Structure

project/
│
├── app.py # Main Flask application
├── heroes.db # SQLite database (generated after first run)
├── templates/
│ ├── base.html # Common layout
│ ├── index.html # Home page for managing heroes
│ ├── add_power.html # Form to add new powers
│ ├── assign_power.html # Form to assign powers to heroes
│ ├── edit.html # Edit hero details
│ ├── edit_power.html # Edit existing power
│ ├── update_power.html # Edit strength/power assignment
└── static/
└── CSS files for styling


---

## How to Use

### 1. **Install Dependencies**

Make sure you have Python 3 installed. Then install Flask and SQLAlchemy:

```bash
pip install flask flask_sqlalchemy

## Run the App
python app.py

## Routes Summary
| Route                    | Method    | Description                    |
| ------------------------ | --------- | ------------------------------ |
| `/`                      | GET, POST | Home page. Add and view heroes |
| `/delete/<int:id>`       | GET       | Delete a hero                  |
| `/update/<int:id>`       | GET, POST | Edit hero name or supername    |
| `/add_power`             | GET, POST | Add a new power                |
| `/edit_power/<int:id>`   | GET, POST | Edit a power                   |
| `/delete_power/<int:id>` | GET       | Delete a power                 |
| `/assign_power`          | GET, POST | Assign a power to a hero       |
| `/update_power/<int:id>` | GET, POST | Edit assigned power/strength   |
| `/delete_power/<int:id>` | GET       | Remove a power assignment      |


