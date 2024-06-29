
from flask import Flask, render_template, request, redirect, url_for


import os


import database as db



template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  


template_dir = os.path.join(template_dir, 'src', 'templates')


app = Flask(__name__, template_folder = template_dir)


@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM afiliados")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    inserObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        inserObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=inserObject)


@app.route('/user', methods=['POST'])
def addUser():
    tipo = request.form['tipo']
    nombre = request.form['nombre']
    vencimientoFactura = request.form['vencimientoFactura']
    afiliado = request.form['afiliado']
    numeroAfiliado = request.form['numeroAfiliado']
    plan = request.form['plan']


    if tipo and nombre and vencimientoFactura and afiliado and numeroAfiliado and plan:
        cursor = db.database.cursor()
        sql= "INSERT INTO afiliados (tipo, nombre, vencimientoFactura, afiliado, numeroAfiliado, plan) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (tipo, nombre, vencimientoFactura, afiliado, numeroAfiliado, plan)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/eliminar/<string:id>')
def eliminar(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM afiliados WHERE id=%s"
    data =(id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))


@app.route('/editar/<string:id>', methods=['POST'])
def editar(id):
    tipo = request.form['tipo']
    nombre = request.form['nombre']
    vencimientoFactura = request.form['vencimientoFactura']
    afiliado = request.form['afiliado']
    numeroAfiliado = request.form['numeroAfiliado']
    plan = request.form['plan']

    if tipo and nombre and vencimientoFactura and afiliado and numeroAfiliado and plan:
        cursor = db.database.cursor()
        sql= "UPDATE afiliados SET tipo =%s, nombre = %s, vencimientoFactura = %s, afiliado = %s, numeroAfiliado = %s, plan =%s WHERE id = %s"
        data = (tipo, nombre, vencimientoFactura, afiliado, numeroAfiliado, plan, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)


