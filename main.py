from flask import Flask, render_template, jsonify

app = Flask(__name__)

TEAMS = [
  {
    'id':1,
    'Name':'Arsenal',
    'Points':66,
    'GD': '+37'
  },
  {
    'id':2,
    'Name':'Manchester City',
    'Points':61,
    'GD': '+42'
  },
  {
    'id':3,
    'Name':'Manchester United',
    'Points':50,
    'GD': '+8'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html', teams=TEAMS)

@app.route("/api/teams")
def list_teams():
  return jsonify(TEAMS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)