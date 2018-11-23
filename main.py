from flask import (Flask,
                   render_template,
                   redirect,
                   url_for,
                   request
                   )
from models.user import User
app = Flask('app')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/user', methods=['POST', 'GET'])
def user():
  data = dict(request.form.items())
  if data.get('name',None):
    models.User.create(
      name=data.get('name', 'anonymous'),
      email=data.get('email', 'Jane@Doe'),
      number=data.get('phone number', '58258')
    )
  return render_template("user.html")


@app.route('/sign', methods=['POST', 'GET'])
def sign():
  data = dict(request.form.items())
  if data.get('name',None):
    models.Sign.create(
      name=data.get('name', 'anonymous'),
      email=data.get('email', 'Jane@Doe'),
      number=data.get('phone number', '58258')
    )
  return render_template("sign.html")




app.run(debug=True, host='0.0.0.0', port=8080)