from flask import Flask, render_template, jsonify
from database import load_teams_from_db, load_team_from_db

app = Flask(__name__)

@app.route("/")
def hello_world():
  teams = load_teams_from_db()
  return render_template('home.html', teams=teams)

@app.route("/api/teams")
def list_teams():
  teams = load_teams_from_db()
  return jsonify(teams)

@app.route("/team/<id>")
def show_team(id):
  team = load_team_from_db(id)

  if not team:
    return "Not Found", 404
  
  return render_template('teampage.html', 
                         team=team)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)