# import Flask class from flask module
from flask import Flask, render_template  
# app is an object of the Flask class. Importing functionality from the module
app = Flask(__name__)  

# path after the / in the domain name
# pass in the name of the main page to render
@app.route("/")  
def hello_world():
  return render_template('home.html') 


### for testing only
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
