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
db = client.flask_db
todos = db.todos


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        category = request.form['category']
        todos.insert_one({'content': content, 'degree': degree, 'category': category})
        return redirect(url_for('index'))

    return render_template('index.html', title='First Page')

@app.route("/catalog")
def view_catalog():
    all_todos = todos.find()
    return render_template("index.html", todos=all_todos, title="Catalog")

# @app.route("/second")
# def view_second_page():
#     return render_template("index.html", title="Second page")

if __name__ == '__main__':
    app.run(debug=True)
