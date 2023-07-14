# import Flask class from flask module
from flask import Flask, render_template, jsonify
# app is an object of the Flask class. Importing functionality from the module
app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Singapore',
}, {
  'id': 2,
  'title': 'Front End Engineer',
  'location': 'Remote, USA',
  'salary': '6600 USD'
}, {
  'id': 3,
  'title': 'Database Administrator',
  'location': 'Ho Chi Minh, Vietnam',
  'salary': '6300 USD'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Remote, Denmark',
  'salary': '44,546 DKK'
}, {
  'id': 4,
  'title': 'Data Scientist',
  'location': 'Sydney, Australia',
  'salary': '9500 AUD'
}]


# path after the / in the domain name
# pass in the name of the main page to render
@app.route("/")
def hello_world():
  # pass the list of jobs and company into home.html as an argument to be dynamic in home.html using {{}}
  return render_template('home.html', jobs=JOBS, company='Maple Leaf')


# instead of returning a list, now we get the list in json format like in any API
# we create a second route /jobs in the URL
# it is an endpoint to return the data to requester for consumption in json and not only HTML
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


### for testing only
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
