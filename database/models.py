from peewee import *
from datetime import datetime as dt
import psycopg2

# db = SqliteDatabase('nid.db')
db = PostgresqlDatabase('df4u2hod95hlv0', user='xxzhjdzfhkzcff', password='e0ccef1e059f71975c415a7a5ec8031d074c3ffe6f3d0f6d3f8bdd52b34fbeab', host='ec2-44-206-137-96.compute-1.amazonaws.com', port=5432)

class BaseModel(Model):
    class Meta:
        database = db


class NID(BaseModel):
    id = PrimaryKeyField()
    nid = IntegerField()
    dob = DateField()
    date = DateTimeField(default=dt.now())

