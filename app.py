import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    "Show Homepage"
    return render_template('home.html', home=home)

@app.route('/about')
def about():
  return render_template('about.html', about=about)

@app.route('/signup')
def signup():
  return render_template('signup.html', signup=signup)

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