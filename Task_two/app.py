from flask import Flask, request, render_template, redirect, flash
import os
import dotenv
import mysql.connector
from mysql.connector import Error
import datetime
app = Flask(__name__)
app.secret_key = "Light Bringer"
dotenv.load_dotenv(r"C:\Users\HP\Documents\.env")
password = os.environ.get("db_password")


try:
    connection = mysql.connector.connect(
        host="localhost", user="root", password=password, database="hng_task_one")
    print("Connection to database established")
except Error as err:
    print(err)


@app.route("/", methods=["GET", "POST"])
def index():
    people_query = """
    select id, people_name, email, phone_number from people;
    """
    cursor = connection.cursor()
    cursor.execute(people_query)
    records = cursor.fetchall()
    
    print(records)
    return render_template ("index.html", records = records )

    
    # return render_template("index.html")

@app.route("/insert", methods = ["GET", "POST"])
def insert():
    if request.method == "POST":
        flash("Data inserted Successfully")
        name = request.form.get("name")
        email = request.form.get("email")
        phone_number = request.form.get("phone")

        people_query = """
        insert into people(people_name, email, phone_number)
        values(%s, %s, %s)
        """
        try:
            cursor = connection.cursor()
            cursor.execute(people_query, (name, email, phone_number))
            connection.commit()
        except Error as err:
            print(err)
    return redirect("/")

@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = connection.cursor()
        cur.execute("""
               UPDATE people
               SET people_name=%s, email=%s, phone_number=%s
               WHERE id=%s
            """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        connection.commit()
    return redirect("/")

@app.route("/delete/<string:id_data>", methods =["GET"])
def delete(id_data):
    flash("Record has been deleted Successfully")
    cur = connection.cursor()
    cur.execute("DELETE FROM people WHERE id=%s", (id_data,))
    connection.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)
