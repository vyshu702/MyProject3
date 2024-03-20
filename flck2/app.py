from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/',methods=['GET'])
def homepage():
    return 'you are in homepage'

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

#to open th login form
@app.route('/index2',methods=['GET'])
def login():
    return render_template('index2.html')

#to recieve the form data
@app.route('/login-form',methods=['POST'])
def login_form_data():
    num1= request.form['x_val']
    num2= request.form['y_val']
    return [int(num1)+int(num2)]

#--------------------------------------------------------------------
#ADDITION
@app.route('/add',methods=['GET'])
def addition():
    return render_template('add.html')

@app.route('/add-form',methods=['POST'])
def add():
    num1= request.form['x_val']
    num2= request.form['y_val']
    return [int(num1)+int(num2)]

#--------------------------------------------------------------------
#subtarction
@app.route('/sub',methods=['GET'])
def subtraction():
    return render_template('sub.html')

@app.route('/sub-form',methods=['POST'])
def sub():
    num1= request.form['x_val']
    num2= request.form['y_val']
    return [int(num1)-int(num2)]
#-------------------------------------------------------------------
#multiplication
@app.route('/mul',methods=['GET'])
def multiplication():
    return render_template('mul.html')

@app.route('/mul-form',methods=['POST'])
def mul():
    num1= request.form['x_val']
    num2= request.form['y_val']
    return [int(num1)*int(num2)]
#---------------------------------------------------------------------
#division
@app.route('/div',methods=['GET'])
def division():
    return render_template('div.html')

@app.route('/div-form',methods=['POST'])
def div():
    num1= request.form['x_val']
    num2= request.form['y_val']
    return [int(num1)/int(num2)]
app.run()