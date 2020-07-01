# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:02:46 2020

@author: Onur Sercan Yılmaz
"""
"""
#Flask URL yapısı ve Dinamik URL Tanımlama

from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "Home"
@app.route("/search")
def search():
    return "Search"
@app.route("/item/<string:id>")
def item(id):
    return "ID: "+ id
@app.route("/delete")
def delete():
    return "DELETED::**:"

if __name__ == "__main__":
    app.run(debug = True) 
    """
    
#%%
"""
#Jinja Template 

from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", number = 10, number2 = 20)
    
if __name__ == "__main__":
    app.run(debug = True) 
 """   
#%%
"""
#Template Koşullu durumlar ve döngüler


from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    message = "Hoş geldiniz!"
    numbers = [1,2,3,4,5,6]
    return render_template("index.html", message=message, numbers = numbers)
    
if __name__ == "__main__":
    app.run(debug = True) 
    """
#%%
"""
#Get ve Post Requestleri    
    
from flask import Flask, render_template,request

app = Flask(__name__)
@app.route("/")
def index():
    message = "Hoş geldiniz!"
    numbers = [1,2,3,4,5,6]
    return render_template("index.html", message=message, numbers = numbers)
    
@app.route("/toplam", methods = ["GET", "POST"])
def toplam():
    if request.method=="POST":
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")
        return render_template("number.html", total = int(number1) + int(number2))
    else:
        return render_template("number.html")
    
if __name__ == "__main__":
    app.run(debug = True) 
    """
  #%%
#Redirect URL işlemi, sayfa yönlendirme

      
from flask import Flask, render_template,request,redirect, url_for

app = Flask(__name__)
@app.route("/")
def index():
    message = "Hoş geldiniz!"
    numbers = [1,2,3,4,5,6]
    return render_template("index.html", message=message, numbers = numbers)
    
@app.route("/toplam", methods = ["GET", "POST"])
def toplam():
    if request.method=="POST":
        number1 = request.form.get("number1")
        number2 = request.form.get("number2")
        return render_template("forredirecturl.html", total = int(number1) + int(number2))
    else:
        return redirect(url_for("index"))
    
if __name__ == "__main__":
    app.run(debug = True) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    