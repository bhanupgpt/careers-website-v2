from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

# JOBS = [
#   {
#     'id': 1,
#     'title': 'Data Analyst',
#     'location': 'Bengaluru, India',
#     'salary': 'Rs. 12,00,000'
#   },
#   {
#     'id': 2,
#     'title': 'Front End Engineer',
#     'location': 'Delhi, India',
#     'salary': 'Rs. 10,00,000'
#   },
#   {
#     'id': 3,
#     'title': 'Data Scientist',
#     'location': 'Remote',
#     'salary': 'Rs. 15,00,000'
#   },
#   {
#     'id': 4,
#     'title': 'Backend Engineer',
#     'location': 'San Francisco, USA',
#     'salary': '120,000 USD '
#   },
# ]


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


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
