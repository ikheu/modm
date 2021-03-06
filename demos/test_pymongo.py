from pymongo import MongoClient

from sys import path
path.append('../')

from modm import field, PymongoCollection, Model

db = MongoClient().test
dbop = PymongoCollection(db)

@dbop.bind('user')
class User(Model):
    name = field.StrField(unique=True)
    age = field.IntField(require=True, default=None)
    country = field.StrField(require=False, default="China")


if __name__ == '__main__':
    User.drop()
    User.ensure_unique()
    u1 = User(name='Bob', age=11)
    u2 = User(name="Bob1", age=12)
    u1.commit()
    u2.commit()
    print(list(User.find()))
