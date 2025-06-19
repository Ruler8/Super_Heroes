# Super_Heroes

# Superhero Registration Flask App

This is a simple Flask web application that allows users to register superheroes by entering a real name and a superhero name. The app supports adding, listing, and editing hero entries using an SQLite database via SQLAlchemy.

---

## Features

- Add new heroes with real name and superhero alias
- List all registered heroes in a table
- Edit existing hero information
- Styled with basic CSS (form, table, buttons)
- Persistent storage using SQLite

---

## Project Structure
superhero-app/
├── app.py # Main Flask application
├── heroes.db # SQLite database (auto-created)
├── static/
│ └── styles.css # CSS styling for the app
├── templates/
│ ├── base.html # Base layout template
│ ├── index.html # Home page (add & view heroes)
│ └── edit.html # Edit hero form
└── README.md # This file

## Create and activate a virtual environment
python3 -m venv heroes
source venv/bin/activate

## Install required packages
pip install flask flask_sqlalchemy

## Running the App
python app.py

## How It Works
## Add a Hero
On the home page:

Fill in the hero's real name and superhero name.

Click "Add Hero" to save it to the database.

View & Edit Heroes
Registered heroes appear in a table.

Each hero has a "Powers" link (you can customize this).

You can also navigate to /update/<hero_id> to edit hero details.

## Styling
Basic CSS is stored in static/styles.css and includes:

Form styling

Table layout

Button-like anchor tags (a.button)



