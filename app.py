#export FLASK_APP=app
#export FLASK_ENV=development

from unicodedata import category
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)

#username = doadmin
#password = 42g3Bp97oia615Ud hide
#host = mongodb+srv://db-mongodb-nyc3-38262-89cd3ee9.mongo.ondigitalocean.com
#database = admin

client = MongoClient('mongodb+srv://doadmin:42g3Bp97oia615Ud@db-mongodb-nyc3-38262-89cd3ee9.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-nyc3-38262')
db = client.productosTotal
todos = db.todos


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content  = request.form['content']
        tipo = request.form['tipo']
        price = request.form['price']
        notes = request.form['notes']
        model = request.form['model']
        velocity = request.form['velocity']
        amper = request.form['amper']
        todos.insert_one({'content': content, 'tipo': tipo, 'price': price, 'notes': notes, 'model': model, 'velocity': velocity, 'amper': amper})
        return redirect(url_for('index'))

    return render_template('index.html', title='First Page')

@app.route("/catalog", methods = ['GET'])
def view_catalog():
    all_todos = todos.find()#todos.find({},{"producto":1,"tipo":1,"price":1,"notes":1,"model":1,"velocity":1,"amper":1})
    return render_template("index.html", todos=all_todos, title="Catalog")

# @app.route("/second")
# def view_second_page():
#     return render_template("index.html", title="Second page")

if __name__ == '__main__':
    app.run(debug=True)
