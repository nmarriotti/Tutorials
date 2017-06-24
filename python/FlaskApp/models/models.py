from peewee import *
import datetime

# Load Database
db = SqliteDatabase('database/posts.db')

class Users(Model):
	id = PrimaryKeyField()
	username = CharField()
	password = CharField()
	role = CharField(default = "user")

	class Meta:
		database = db

class Post(Model):
	id = PrimaryKeyField()
	date = DateTimeField(default = datetime.datetime.now)
	title = CharField()
	text = TextField()

	class Meta:
		database = db

def initialize_db():
	db.connect()
	db.create_tables([Post, Users], safe=True)

initialize_db