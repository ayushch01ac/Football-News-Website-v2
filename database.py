from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://rubmbxvy7i8fhv5lw9sk:pscale_pw_z7hErJlZPLLTXreeFkA1r2Pp33R7fZDAVieMTla9ndW@ap-south.connect.psdb.cloud/footballnews?charset=utf8mb4",      
connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"}
})

with engine.connect() as conn:
  result = conn.execute(text("select * from teams"))
  print(result.all())