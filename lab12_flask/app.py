"""
Makhai Morgan
Oct 27, 2025
lab 12, introduction to Flask
"""
from flask import Flask,    render_template, url_for, redirect

"""
create an object 'app' from the Flask module.
__name__ set to __main__ if the script is running directly from the main file
"""
app = Flask(__name__)

# set the routing to the main page
#'route' decorator is used to access the root URL
@app.route('/')
def index():
    name = "Makhai Morgan"
    fruits = ["apple", "kiwi", 'orange']
    checkfruit = 'pineapple'
    return render_template("index.html", username = name, fruits_list = fruits, c = checkfruit)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/quotes')
def quotes():
    return render_template("quotes.html")

@app.route('/login')
def login():
    return redirect(url_for('index'))

# set the 'app' to run if you execute the file directly(not when it is imported)
if __name__ == "__main__":
    app.run(debug=True)