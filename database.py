import os
from sqlalchemy import create_engine, text

connection_string = os.environ['DB_CONNECTION_STRING']

#SSL passed as a dict with one key ssl
engine = create_engine(connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

#store the database objects into a dict
#_mapping is to extract the data for each row as a dictionary and append it to the result_dicts[]
#def load_jobs_from_db():
#with engine.connect() as conn:
#result = conn.execute(text("select * from jobs"))
#jobs = []
#for row in result.all():
#jobs.append(dict(row._mapping))
#return (jobs)


#load jobs for the page and search
def load_jobs_from_db(search_query=None):
  with engine.connect() as conn:
    if search_query:
      # Use named placeholders in the SQL query and sanitize the input
      sql = text(
        "SELECT * FROM jobs WHERE title LIKE :query OR location LIKE :query")
      parameters = {"query": f"%{search_query}%"}
      result = conn.execute(sql, parameters)
    else:
      result = conn.execute(text("SELECT * FROM jobs"))

    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs


# :val is string formatting in sqlalchemy to specify something that needs to be filled in and it comes from te URL in the path in app.py when user clicks to view
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id={id}"))
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])


# inserting forms values into DB
# :column name is a variable
# using the jobs as a dictionary in app.py to pass to the using request.form
# error "Connection.execute() got an unexpected keyword argument 'job_id'" was because in SQLAlchemy 2.0 the parameters have to be sent as a dict instead (row)
def add_application_to_db(job_id, data):
  row = {
    "job_id": job_id,
    "full_name": data["full_name"],
    "email": data["email"],
    "linkedin_url": data["linkedin_url"],
    "education": data["education"],
    "work_experience": data["work_experience"],
    "resume_url": data["resume_url"],
  }
  with engine.connect() as conn:
    sql = text(
      "INSERT INTO applications(job_id,full_name,email,linkedin_url,education,work_experience,resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )
    conn.execute(sql, row)
    conn.commit()
