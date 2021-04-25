from flask import Flask, render_template, request
from flask.helpers import url_for
import skiplist

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('landing.html')

@app.route('/constructform')
def construct_page():
    return render_template('constructform.html')

@app.route('/constructform' , methods=['POST'])
def construction():
    elements = request.form.get("elements", type=str, default=0)
    l = list(map(int,elements.split(' ')))
    skiplist.main(l)
    return render_template('display.html')
    

@app.route('/display')
def display_page():
    return render_template('display.html')

@app.route('/menu')
def menu_page():
    return render_template('menu.html')

@app.route('/insert')
def insert_page():
    return render_template('insertform.html')

@app.route('/delete')
def delete_page():
    return render_template('deleteform.html')

@app.route('/search')
def search_page():
    return render_template('searchform.html')

@app.route('/viewadt')
def viewadt():
    return render_template('view_adt.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False) 