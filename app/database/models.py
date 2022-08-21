from peewee import *
from datetime import datetime as dt


# db = SqliteDatabase('nid.db')
db = PostgresqlDatabase('my_app', user='postgres', password='secret',
                           host='10.1.0.9', port=5432)

class BaseModel(Model):
    class Meta:
        database = db


class NID(BaseModel):
    id = PrimaryKeyField()
    nid = IntegerField()
    dob = DateField()
    date = DateTimeField(default=dt.now())

