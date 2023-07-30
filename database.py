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
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return (jobs)


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
