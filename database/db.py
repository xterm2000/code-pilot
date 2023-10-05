import peewee

DATABASE_NAME = 'pilot'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'postgres12#'
DATABASE_HOST = '192.168.68.200'
DATABASE_PORT = 30032

db = peewee.PostgresqlDatabase(
  database=DATABASE_NAME,
  user=DATABASE_USER,
  password=DATABASE_PASSWORD,
  host=DATABASE_HOST,
  port=DATABASE_PORT
)

