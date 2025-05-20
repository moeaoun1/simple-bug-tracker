from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory bug list for now
bugs = []

@app.route('/')
def index():
    return render_template('index.html', bugs=bugs)

@app.route('/add', methods=['GET', 'POST'])
def add_bug():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        bugs.append({
            'title': title,
            'description': description,
            'priority': priority,
            'status': 'Open'
        })
        return redirect(url_for('index'))
    return render_template('add_bug.html')

@app.route('/resolve/<int:bug_id>')
def resolve_bug(bug_id):
    if 0 <= bug_id < len(bugs):
        bugs[bug_id]['status'] = 'Resolved'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

