from peewee import (CharField,
                    SqliteDatabase,
                    Model,
                    TextField,
                    DateTimeField,
                    IntegrityError)
import datetime
db = SqliteDatabase("starTech.db")

user = [
    {'name': 'A new entry', 'body': 'This is a body'},
    {'name': 'Another entry', 'body': 'A post body'}
]


class User(Model):
    title = CharField(default='title', max_length=255, unique=True)
    body = TextField(default='A post body')
    entrytime = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def user(cls, name, body):
        try:
            User.create(
                name=name,
                body=body
            )
        except IntegrityError:
            pass

    @classmethod
    def list(cls):
        initialize()
        user = User.select()
        return user


    class Meta:
        database = db


def initialize():
    db.create_tables([User], safe=True)
    for user in User:
        try:
            User.create(
                name=user.get('title'),
                user=user.get('body')
            )
        except IntegrityError:
            pass