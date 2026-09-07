from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.String(200), nullable=True)
    text = db.Column(db.Text, nullable=False)
    

# Главная страница
@app.route("/")
def index():
    return render_template("index.html")

# Страница дневника
@app.route("/notes", methods=["GET", "POST"])
def notes():
    
    if request.method == "POST":
        title = request.form["title"]
        subtitle = request.form["subtitle"]
        text = request.form["text"]

        note = Notes(title=title, 
                     subtitle=subtitle, 
                     text=text)

        db.session.add(note)
        db.session.commit()

        return redirect(url_for("notes"))

    notes = Notes.query.all()
    
    return render_template("notes.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)
