import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://bob:1234@127.0.0.1:5432/postgres')
engine.connect()
