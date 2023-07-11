from flask import Flask ### import Flask class from flask module

app = Flask(__name__) ### app is an object of the Flask class. Importing functionality from the module

@app.route("/") ### path after the / in the domain name
def hello_world():
    return "<p>Hello, World!</p>"

### for testing only
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  