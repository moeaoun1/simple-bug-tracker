# Simple Bug Tracker

A lightweight web app for submitting and tracking bugs. Built with Flask and designed to demonstrate backend development using Python, form handling, and template rendering.

## 🔧 Features
- Submit a bug with title, description, and priority
- View a list of active and resolved bugs
- Mark bugs as resolved
- Simple in-memory list (SQLite version coming soon)

## 🧱 Stack
- Python 3
- Flask
- HTML/CSS
- Jinja2 Templating

## 🚀 Setup Instructions

```bash
git clone https://github.com/moeaoun1/simple-bug-tracker.git
cd simple-bug-tracker
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
