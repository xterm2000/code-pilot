import peewee
from database.db import BaseModel


class Project(BaseModel):
  project_id = peewee.AutoField(primary_key=True)
  project_name = peewee.CharField()
  description = peewee.TextField()
  created_at = peewee.DateTimeField()
  updated_at = peewee.DateTimeField()
  stage = peewee.CharField()
