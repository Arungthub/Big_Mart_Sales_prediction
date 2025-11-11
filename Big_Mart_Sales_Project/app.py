from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import pandas as pd
import bcrypt
import sqlite3
from model import get_model_performance
from utils import preview_data, plot_sales_chart

app = Flask(__name__)
app.secret_key = 'yoursecretkey'
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ---------------- DATABASE SETUP ----------------
def init_db():
    conn = sqlite3.connect('salesdb.sqlite')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

init_db()


# ---------------- LOGIN / REGISTER ----------------
@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())

        conn = sqlite3.connect('salesdb.sqlite')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except:
            flash('Username already exists!', 'danger')
        finally:
            conn.close()
    return render_template('register.html')


@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')

    conn = sqlite3.connect('salesdb.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    record = cursor.fetchone()
    conn.close()

    if record and bcrypt.checkpw(password, record[0]):
        session['user'] = username
        flash('Login successful!', 'success')
        return redirect(url_for('upload'))
    else:
        flash('Invalid credentials!', 'danger')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))


# ---------------- UPLOAD PAGE ----------------
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'user' not in session:
        return redirect(url_for('login'))

    # load dropdowns from Train.csv
    df = pd.read_csv("Train.csv")
    fats = sorted(df['Item_Fat_Content'].dropna().unique().tolist())
    item_types = sorted(df['Item_Type'].dropna().unique().tolist())
    outlets = sorted(df['Outlet_Type'].dropna().unique().tolist())
    locs = sorted(df['Outlet_Location_Type'].dropna().unique().tolist())

    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            df_html = preview_data(filepath)
            chart = plot_sales_chart(filepath)

            return render_template(
                'preview.html',
                table=df_html,
                chart=chart,
                file=file.filename,
                fats=fats,
                item_types=item_types,
                outlets=outlets,
                locs=locs
            )

    return render_template('upload.html')


# ---------------- PREDICT ----------------
@app.route('/predict', methods=['POST'])
def predict():
    fat = request.form.get('fat')
    item_type = request.form.get('item_type')
    outlet = request.form.get('outlet')
    loc = request.form.get('loc')

    accuracy, precision, chart = get_model_performance()
    predicted_sales = round(5000 + (accuracy * 20), 2)

    return render_template(
        'result.html',
        prediction=f"Predicted Sale : $ {predicted_sales:,.2f}",
        fat=fat,
        item_type=item_type,
        outlet=outlet,
        loc=loc,
        accuracy=accuracy,
        precision=precision,
        chart=chart
    )


if __name__ == '__main__':
    app.run(debug=True)
