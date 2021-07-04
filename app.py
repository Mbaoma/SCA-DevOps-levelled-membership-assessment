import mysql.connector
from flask import *


def load_config():
    with open("config.json") as f:
        config = json.load(f)
    return config

app = Flask(__name__)
config = load_config()

app.secret_key = config["secret_key"]

# Below is the db connection, it is advisable to 
# initiate a new connection for each new route
# without initiating for the entire application for security purpose
db = mysql.connector.connect(**config["db"])
cursor = db.cursor(dictionary=True)



"""
EXAMPLE of initiating connection within route
--------------------------------------------------
NB: if you are doing this, you dont need to do it at the top of your script




@app.route("/login/", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        email = request.form.get("email", "").lower()
        password = request.form.get("password", "")
        db = mysql.connector.connect(**config["db"])
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s", 
            (email, password))
        user = cursor.fetchone()
        if user:
            if user["active"]:
                session["user"] = user["id"]
                session.permanent = True
                return redirect(url_for("dashboard"))
    return render_template("login.html", **config)


@app.errorhandler(404)
@app.errorhandler(405)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
"""