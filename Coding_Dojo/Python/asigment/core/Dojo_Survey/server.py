from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "doesitevenneedone"

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    if len(request.form["name"])<1:
        flash("Name can't be empty")
        return redirect("/")
    if len(request.form["comments"])<1:
        flash("Comment can't be empty")
        return redirect("/")
    else:
        name = request.form["name"]
        location = request.form["location"]
        fav_language = request.form["favlanguage"]
        comments = request.form["comments"]
        return render_template("result.html", name = name, location = location, fav_language = fav_language, comments = comments)

    


@app.route("/danger")
def danger_back():
    print("someone visited '/danger'.'")
    return redirect("/")

    

if __name__=="__main__":
    
    app.run(debug=True, port = 8000) 