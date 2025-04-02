from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "LANE"
mydb = mysql.connector.connect(
    host="localhost",  # e.g., "localhost"
    user="root",
    password="LANE",
    database="student_registration"
)

mycursor = mydb.cursor()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        email = request.form["email"]
        phone = request.form["phone"]
        dob = request.form["dob"]
        address = request.form["address"]

        sql = "INSERT INTO users (fname, lname, email, phone, dob, address) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (fname, lname, email, phone, dob, address)
        mycursor.execute(sql, val)
        mydb.commit()

        return "Data submitted successfully!"  # Or redirect to a thank you page
    return render_template("index.html")  # Render the HTML form


@app.route("/submit_form", methods=["POST"])  # Correct route for form submission
def submit_form():
    fname = request.form["fname"]
    lname = request.form["lname"]
    email = request.form["email"]
    phone = request.form["phone"]
    dob = request.form["dob"]
    address = request.form["address"]

    sql = "INSERT INTO users (fname, lname, email, phone, dob, address) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (fname, lname, email, phone, dob, address)
    mycursor.execute(sql, val)
    mydb.commit()

    return "Data submitted successfully!"  # Or redirect


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    mycursor.execute("SELECT * FROM users")
    users = mycursor.fetchall()
    return render_template("admin.html", users=users)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "password": # Replace with actual secure authentication
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
