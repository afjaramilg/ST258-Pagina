from flask import Flask, request, url_for, redirect, abort, render_template
import mysql.connector

app = Flask(__name__)

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flask"
)

cursor = midb.cursor(dictionary=True)

@app.route('/')
def index():
    return "hola mundo"

@app.route('/lala/<usuario>', methods=['GET', 'POST'])
def lala(usuario):
    return f"{usuario}"

@app.route('/lele', methods=['POST', 'GET'])
def lele():
    cursor.execute('select * from Usuario')
    usuarios = cursor.fetchall()
    #abort(403)
    #return redirect(url_for("lala", usuario=23))
    #a=url_for("lala", usuario=23)

    #return f"{a}"
    #return render_template("lele.html")
    #return {
    #    "luis": "Bernardo",
    #    "andres":"jaramillo"
    #}
    return render_template('lele.html', usuarios=usuarios)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html',message="hola")

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == "POST":
        username = request.form['User']
        password = request.form['Password']
        correo = request.form['Correo']
        sql = "insert into usuario (User, Password, Correo) values (%s, %s, %s)"
        values = (username, password, correo)
        cursor.execute(sql,values)
        midb.commit()
        return redirect(url_for('lele'))
    return render_template('crear.html')