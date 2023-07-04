from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssla_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    results_as_dict = result.mappings().all()
    jobs = []
    for row in results_as_dict:
      jobs.append(row)
    return jobs


def load_job_page_from_db(id):
  with engine.connect() as conn:
    val = id
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {val}"))
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    full_name = data['full_name']
    email = data['email']
    linkedin_url = data['linkedin_url']
    education = data['education']
    work_experience = data['work_experience']
    resume_url = data['resume_url']
    conn.execute(
      text(
        f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ({job_id}, '{full_name}', '{email}', '{linkedin_url}', '{education}', '{work_experience}', '{resume_url}')"
      ))
