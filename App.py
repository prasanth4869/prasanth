#pip install flask
from flask import Flask, render_template as r, request,redirect, url_for
app=Flask(__name__)
@app.route("/")
def index():
    return r("Home.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    message=""
    if request.method=="POST" and 'name' in request.form and 'uid' in request.form and 'email' in request.form and 'pass' in request.form and 'gn' in request.form:
        FullName=request.form["name"]
        UserId = request.form["uid"]
        Email = request.form["email"]
        Password = request.form["pass"]
        Gender = request.form["gn"]
        message="Successfull you filled application"
        return r("Login.html", msg=message)
    else:
        message="Please fill all the field in application"
    return r("Register.html", msg=message)
#
# @app.route("/insert", methods=['POST','GET'])
# def insert():
#     if request.method=='POST':
#         name=request.form['name']
#         userid = request.form['uid']
#         password = request.form['pass']
#
#         return f'Name: {name}, UserId: {userid}, Password: {password}'
#     else:
#
#         return redirect(url_for('register'))


if __name__=='__main__':
    app.run(debug=True)
