from flask import Flask, render_template

app = Flask(__name__)

@app.route('/fruits')
def show_fruits():
    fruits = ['Apple','Banana','Cherry','Date','Elderberry']
    return render_template('fruits_list.html',fruits=fruits)