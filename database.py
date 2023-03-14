from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,      
connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"}
})


def load_teams_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from teams"))
    teams = []
    for row in result.all():
      teams.append({'id':row.id, 'Name':row.team_name, 'Points':row.points})
    return teams

def load_team_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM teams WHERE id = {}".format(id)),
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return {'id':rows[0].id, 'Name':rows[0].team_name, 'Points':rows[0].points}


