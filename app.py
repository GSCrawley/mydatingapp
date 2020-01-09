import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for
host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/mydatingapp')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
users = db.users

app = Flask(__name__)


@app.route('/')
def home():
    "Show Homepage"
    return render_template('home.html', home=home)

@app.route('/about_you')
def about_you():
  return render_template('about_you.html', about_you=about_you)

@app.route('/user_list', methods=['POST'])
def user_list():
  return render_template('user_list.html', user_list=user_list)

@app.route('/user_details')
def user_details():
  return render_template('user_details.html', user_details=user_details)

@app.route('/signup')
def signup():
  return render_template('signup.html', signup=signup)

@app.route('/signup', methods=['POST'])
def signup_submit():
    user = {
        'name': request.form.get('username'),
        'email': request.form.get('email'),
        'password': request.form.get('password')
    }
    print(user)
    user_id = users.insert_one(user).inserted_id
    return redirect(url_for('about_you'))

@app.route('/login')
def login():
  return render_template('login.html', login=login)

@app.route('/profiles')
def profiles():
  return render_template('profiles.html', profiles=profiles)

@app.route('/video')
def video():
  return render_template('video.html', video=video)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))