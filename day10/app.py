from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_data():
    name = request.form['fname']
    birthday = request.form['bdate']
    birthdate = datetime.strptime(birthday, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return jsonify({'name': name, 'age': age})


app.run(debug=True)