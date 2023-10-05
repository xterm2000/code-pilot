import peewee
from database.db import BaseModel
from database.db import db


class Project(BaseModel):
  project_id = peewee.AutoField(primary_key=True)
  project_name = peewee.CharField()
  description = peewee.TextField()
  created_at = peewee.DateTimeField()
  updated_at = peewee.DateTimeField()
  stage = peewee.CharField()

  class Meta:
    table_name = 'person'


db.create_tables([Project])
db.transaction()
Project.create(project_name='test', description='test',
               created_at='2020-01-01', updated_at='2020-01-01', stage='test')
db.commit()

