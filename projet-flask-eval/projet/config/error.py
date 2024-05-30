from projet import app
from flask import render_template


app.secret_key = "rootardrdt"
app.config['PERMANENT_SESSION_LIFETIME'] = 3600

@app.errorhandler(404)
def page_not_found(e):
    data = {
        "title": "Hello World",
        "body": "Flask simple MVC"
    }
    return render_template('index.html', data = data)