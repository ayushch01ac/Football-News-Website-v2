from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://rubmbxvy7i8fhv5lw9sk:pscale_pw_z7hErJlZPLLTXreeFkA1r2Pp33R7fZDAVieMTla9ndW@ap-south.connect.psdb.cloud/footballnews?charset=utf8mb4",      
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


