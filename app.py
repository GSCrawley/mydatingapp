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
  return render_template('home.html', home=home)

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
    return redirect(url_for('user_info'))

@app.route('/login')
def login():
  return render_template('login.html', login=login)
@app.route('/user_info')
def user_info():
  return render_template('user_info.html', user = {}, user_info=user_info)

@app.route('/users_index', methods=['POST'])
def user_list():                                                                                                                                                                                                                                        
  return render_template('users_index.html', user_list=user_list)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

@app.route('/your_profile')
def your_profile():
  return render_template('your_profile.html', your_profile=your_profile)

@app.route('/user_info', methods=['POST'])        
def user_submit():
  user = {
        # 'user_pic': request.form.get('user_info/pic'),
        'username': request.form.get('user_info/username'),
        'gender': request.form.get('user_info/gender'), 
        "gender you're seeking": request.form.get("user_info/gender you're seeking"),
        'relationship type': request.form.get('user_info/relationship type')
    }
  print(user)
  user_id = user.insert_one(user).inserted_id
  return redirect(url_for('user_show', user_id=user_id))

@app.route('/users/<user_id>')
def users_show(user_id):
    """Show a single user."""
    user = users.find_one({'_id': ObjectId(user_id)})
    return render_template('user_show.html', user=user)

@app.route('/users')
def users():
  return render_template('users.html', users=users)

@app.route('/video')
def video():
  return render_template('video.html', video=video)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))