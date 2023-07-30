# import Flask class from flask module
from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

# app is an object of the Flask class. Importing functionality from the module
app = Flask(__name__)


# path after the / in the domain name
# pass in the name of the main page to render
@app.route("/")
def maple_leaf_index():
  jobs = load_jobs_from_db()
  # pass the list of jobs and company into home.html as an argument to be dynamic in home.html using {{}}
  return render_template('home.html', jobs=jobs)


# instead of returning a list, now we get the list in json format like in any API
# we create a second route /jobs in the URL
# it is an endpoint to return the data to requester for consumption in json and not only HTML
@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return (jsonify(jobs))


# a view for each job. The <id> is to make passing job id dynamic in flask
@app.route("/job/<id>")
def view_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not found", 404
  return render_template('jobpage.html', job=job)


### for testing only
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
