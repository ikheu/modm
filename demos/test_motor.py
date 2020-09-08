import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from sys import path
path.append('../')

from modm import field, Model, MotorCollection
db = AsyncIOMotorClient().test
dbop = MotorCollection(db)


@dbop.bind('user')
class User(Model):
    _id = field.IntField()
    name = field.StrField(unique=True)
    age = field.IntField(require=False, default=None)
    country = field.StrField(require=False, default="China")


if __name__ == '__main__':
    async def test():
        return await User.find({}).to_list(None)
    res = asyncio.get_event_loop().run_until_complete(test())
    print(res)
