modm
======================

A Tiny MongoDB ODM.

Quick example:

```python
from pymongo import MongoClient
from modm import field, PymongoCollection, Model

db = MongoClient().test
dbop = PymongoCollection(db)

@dbop.bind('user')
class User(Model):
    _id = field.IntField()
    name = field.StrField(unique=True)
    age = field.IntField(require=False, default=None)
    country = field.StrField(require=False, default="China")

if __name__ == '__main__':
    User.drop()
    User.ensure_unique()
    u = User(name='Bob', age=11)
    u.commit()
    print(list(User.find()))
```

