from flask import Flask, render_template, request, session 
app = Flask(__name__)


@app.route('/')
def index():
	return render_template("index.html")

@app.route("/more")
def more():
	return render_template("more.html")

@app.route("/thanks", methods=['POST'])
def thanks():
	name = request.form.get("name")
	email = request.form.get("email")
	number = request.form.get("number")
	return render_template("thanks.html",name=name, email=email, phoneNumber=number)

