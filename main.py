from flask import Flask

app = Flask(__name__)
@app.route("/") #to match to home page

def hello_world():
  return "helloshfgdf"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)