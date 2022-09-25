from peewee import *
from datetime import datetime as dt
import psycopg2

# db = SqliteDatabase('nid.db')
db = PostgresqlDatabase('dbs3r62udltj0e', user='yjkegvygujrszw', password='e4f1710da1507220d4b938740075c4dead3ed6e37701a210140d9d991c22f6e7', host='ec2-44-194-4-127.compute-1.amazonaws.com', port=5432)

class BaseModel(Model):
    class Meta:
        database = db


class NID(BaseModel):
    id = PrimaryKeyField()
    nid = CharField(max_length=20)
    dob = DateField()
    date = DateTimeField(default=dt.now())

