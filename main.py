from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_page_from_db, add_application_to_db

app = Flask(__name__)


# to create html route
@app.route("/")  #to match to home page
def hello_world():
  jobs_list = load_jobs_from_db()
  return render_template('index.html', jobs=jobs_list)


# to create api route
@app.route("/api/jobs")
def list_jobs():
  jobs_list = load_jobs_from_db()
  return jsonify(jobs_list)


@app.route("/job/<id>")  #to create a dynamic route
def show_job(id):
  job = load_job_page_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)


@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_job_page_from_db(id)
  return jsonify(job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  add_application_to_db(id, data)
  # send an email
  job = load_job_page_from_db(id)
  return render_template('application_submitted.html',
                         application=data,
                         job=job)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
