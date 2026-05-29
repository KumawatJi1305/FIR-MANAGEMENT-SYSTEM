from flask import Flask, render_template, request, redirect, session
import mysql.connector
from datetime import date
app = Flask(__name__)
app.secret_key = 'your_secret_key'
# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Enter your sql password",
    database="fir_hns"
)
# Home Route
@app.route('/')
def home():
    return render_template('index.html')
# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        if userid == 'HiKe CodeX' and password == '1326':
            session['user'] = userid
            return redirect('/view_fir')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')
# File FIR Route
@app.route('/file_fir', methods=['GET', 'POST'])
def file_fir():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        complaint = request.form['complaint']
        today = date.today()
        status = 'Pending'
        cursor = conn.cursor()
        cursor.execute("INSERT INTO all_firs (name, phone, address, complaint, status, date) VALUES (%s, %s, %s, %s, %s, %s)",
                       (name, phone, address, complaint, status, today))
        conn.commit()
        cursor.close()
        return redirect('/')
    return render_template('file_fir.html')
# View FIR Route
@app.route('/view_fir')
def view_fir():
    if 'user' in session:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM all_firs")
        data = cursor.fetchall()
        cursor.close()
        return render_template('view_fir.html', data=data)
    else:
        return redirect('/login')
#  Edit FIR Route
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_fir(id):
    cursor = conn.cursor()
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        address = request.form["address"]
        complaint = request.form["complaint"]
        status = request.form["status"]
        fir_date = request.form["date"]
        query = "UPDATE all_firs SET name=%s, phone=%s, address=%s, complaint=%s, status=%s, date=%s WHERE id=%s"
        values = (name, phone, address, complaint, status, fir_date, id)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        return redirect("/view_fir")
    cursor.execute("SELECT * FROM all_firs WHERE id=%s", (id,))
    data = cursor.fetchone()
    cursor.close()
    return render_template("edit.html", fir=data)
# Update FIR
@app.route('/update/<int:id>', methods=['POST'])
def update_fir(id):
    name = request.form['name']
    phone = request.form['phone']
    address = request.form['address']
    complaint = request.form['complaint']
    fir_date = request.form['date']
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE all_firs SET name=%s, phone=%s, address=%s, complaint=%s, date=%s WHERE id=%s
    """, (name, phone, address, complaint, fir_date, id))
    conn.commit()
    cursor.close()
    return redirect('/view_fir')
# Run App
if __name__ == '__main__':
    app.run(debug=True)
