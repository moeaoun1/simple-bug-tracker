from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# SQLite DB config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bugs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Bug model
class Bug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Open')

# Ensure DB exists
with app.app_context():
    db.create_all()


# Home page
@app.route('/')
def index():
    bugs = Bug.query.all()
    return render_template('index.html', bugs=bugs)

# Add bug
@app.route('/add', methods=['GET', 'POST'])
def add_bug():
    if request.method == 'POST':
        new_bug = Bug(
            title=request.form['title'],
            description=request.form['description'],
            priority=request.form['priority'],
            status='Open'
        )
        db.session.add(new_bug)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_bug.html')

# Mark bug resolved
@app.route('/resolve/<int:bug_id>')
def resolve_bug(bug_id):
    bug = Bug.query.get_or_404(bug_id)
    bug.status = 'Resolved'
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
