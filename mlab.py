#mongodb://<dbuser>:<dbpassword>@ds027425.mlab.com:27425/techfood
import mongoengine
import json



# mongodb://<dbuser>:<dbpassword>@ds054289.mlab.com:54289/cuonghq

host = "ds054289.mlab.com"
port = 54289
db_name = "cuonghq"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)


def list2json(l):
   return [json.loads(item.to_json()) for item in l]


def item2json(item):
   return json.loads(item.to_json())
