from flask import Flask, render_template, request
from test import *

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/compilar',methods=['POST'])
def compilarT():
    x=ideADK(request.form['texto'])
    if x.compilar()==True :
        return render_template('si.html')
    else:
        return render_template('no.html')
        

if __name__=='__main__':
    app.run(port =3000,debug=True) 