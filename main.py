from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MySQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "user_reg_details"

db = MySQL(app)

class User:
    def __init__(self,name,email,password,cPassword):
        self.name = name
        self.email = email
        self.password = password
        self.cPassword = cPassword


@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/signup",methods=["GET","POST"])
def signup_page():
    if request.method == "POST":
        name = request.form.get("name",type=str)
        email = request.form.get("email",type=str)
        password = request.form.get("password",type=str)
        confirm_pass = request.form.get("cPassword",type=str)

        cursor = db.connection.cursor()
        cursor.execute("INSERT INTO user_registration_data (name,email,password,confirm_pass) values(%s, %s, %s, %s)",(name,email,password,confirm_pass))
        db.connection.commit()
    return render_template("signup.html")

# endpoint to fetch and display all books

@app.route("/books")
def show_books():
    return render_template("booklist.html")

@app.route("/addbook",methods=["GET","POST"])
def add_book_form():
    return render_template("add_book.html")


if __name__ == "__main__":
    app.run(debug=True)