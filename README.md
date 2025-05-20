# Simple Bug Tracker

A lightweight web app to submit and track bugs. Built with Flask and SQLite to demonstrate backend logic, form handling, and template rendering.

## Features
- Submit a bug with title, description, and priority
- View all submitted bugs
- Mark bugs as resolved
- (Coming soon: SQLite database + persistent storage)

## Stack
- Python 3
- Flask
- HTML/CSS
- Jinja2 Templating

## Setup

```bash
git clone https://github.com/moeaoun1/simple-bug-tracker
cd simple-bug-tracker
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
python app.py
