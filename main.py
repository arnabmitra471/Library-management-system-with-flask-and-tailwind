from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/signup",methods=["GET","POST"])
def signup_page():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_pass = request.form.get("cPassword")
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