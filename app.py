from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
import skiplist

app = Flask(__name__)
s = skiplist.skiplist()

@app.route('/')
def welcome():
    return render_template('landing.html')

@app.route('/reset')
def reset():
    s.clear()
    return render_template("landing.html")

@app.route('/constructform')
def construct_page():
    return render_template('constructform.html')

@app.route('/constructform' , methods=['POST'])
def construction():
    elements = request.form.get("elements", type=str)
    l = list(map(int,elements.split(' ')))
    s.construct(l)
    return render_template('menu.html')
    

# @app.route('/display')
# def display_page():
#     return render_template('display.html')

@app.route('/menu')
def menu_page():
    return render_template('menu.html')

@app.route('/insert')
def insert_page():
    return render_template('insertform.html')

@app.route('/insert' , methods=['POST'])
def insertion():
    element = request.form.get("insert_element", type=int)
    s.insert(element)
    return render_template('menu.html')

@app.route('/delete')
def delete_page():
    return render_template('deleteform.html')

@app.route('/delete' , methods=['POST'])
def deletion():
    element = request.form.get("delete_element", type=int)
    s.delete(element)
    return render_template('menu.html')

@app.route('/search')
def search_page():
    return render_template('searchform.html')

@app.route('/search' , methods=['POST'])
def search():
    element = request.form.get("search_element", type=int)
    s.search(element)
    return render_template('menu.html')

@app.route('/viewadt')
def viewadt():
    return render_template('view_adt.html')

if __name__ == '__main__':
    app.run(debug=True) 