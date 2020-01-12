import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for
host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/mydatingapp')
client = MongoClient(host='f{host}?retryWrites=false')
db = client['mydatingapp']
users = db.users

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html', home=home)

@app.route('/')
def users_index():
    """Show all users."""
    return render_template('users_index.html', users=users)                                                                                                                                                                                                                                                                                                                                                                                                                                                            

# @app.route('/login')
# def login():
#     return render_template('login.html', login=login)

# @app.route('/login/user_submit')
#     def user_login()


# @app.route('/signup')
# def signup():
#     return render_template('signup.html', signup=signup)
 
# @app.route('/signup', methods=['POST'])
# def signup_submit():
#     user = {
#         'name': request.form.get('username'),
#         'email': request.form.get('email'),
#         'password': request.form.get('password')
#     }
#     print(user)
#     user_id = users.insert_one(user).inserted_id
#     return redirect(url_for('user_info'))

@app.route('/users/new')
def users_new():
    """Create a new User Profile"""
    return render_template('users_new.html', user={}, title='New User Profile') 

@app.route('/users', methods=['POST'])        
def user_submit():
    """Submit a New User Profile"""
    user = {
        # 'user_pic': request.form.get('user_info/pic'),
        'username': request.form.get('username'),
        'gender': request.form.get('gender'), 
        "gender you're seeking": request.form.get("gender you're seeking"),
        'relationship type': request.form.get('relationship type'),
        'bio': request.form.get('bio')
    
    }
    print(user)
    user_id = users.insert_one(user).inserted_id
    return redirect(url_for('/users_show', user_id=user_id))

@app.route('/users/<user_id>')
def users_show(user_id):
    """Show a single user."""
    user = users.find_one({'_id': ObjectId(user_id)})
    return render_template('users_show.html', user=user)

@app.route('users/<user_id>/edit')
def users_edit(user_id):
    """Show the edit form for a User Profile"""
    user = users.find_one({'_id': ObjectId(user_id)})

@app.route('users/<user_id>', methods=['POST'])
def users_update(users_id):
    """Submit an edited User Profile"""
    updated_profile = {
        'username': request.form.get('name'),
        'relationship': request.form.get('relationship type')
        'gender':
        'gender_preference':
        

    }
    return render_template('users.html', users=users)

@app.route('/video')
def video():
    return render_template('video.html', video=video)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))