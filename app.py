# import Flask class from flask module
from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

# app is an object of the Flask class. Importing functionality from the module
app = Flask(__name__)


# path after the / in the domain name
# pass in the name of the main page to render
@app.route("/")
def hello_maple_leaf():
  jobs = load_jobs_from_db()
  # pass the list of jobs and company into home.html as an argument to be dynamic in home.html using {{}}
  return render_template('home.html', jobs=jobs, company='Maple Leaf')


# instead of returning a list, now we get the list in json format like in any API
# we create a second route /jobs in the URL
# it is an endpoint to return the data to requester for consumption in json and not only HTML
@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return (jsonify(jobs))


### for testing only
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
