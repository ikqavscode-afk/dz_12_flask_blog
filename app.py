from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Хранилище данных дневника
notes_data = {}

# Главная страница
@app.route("/")
def index():
    return render_template("index.html")

# Страница дневника
@app.route("/notes", methods=["GET", "POST"])
def notes():
    
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"]

        notes_data[title] = text

        return redirect(url_for("notes"))
    
    return render_template("notes.html", notes=notes_data)

if __name__ == "__main__":
    app.run(debug=True)
