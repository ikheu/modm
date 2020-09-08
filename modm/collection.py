from functools import wraps
from pymongo import IndexModel


def generater_func(func):
    @classmethod
    @wraps(func)
    def foo(cls, *args, **kwargs):
        return func(*args, **kwargs)
    return foo


class BaseCollection():
    def bind(self, table):
        def func(_class):
            self.__tb__ = self.db[table]
            attr_dict = {}
            for k, v in _class.__dict__.items():
                attr_dict[k] = v
            bases = (*_class.__bases__, self.__class__)
            for key in self.ops:
                attr_dict[key] = generater_func(getattr(self.__tb__, key))
            return type(_class.__name__, bases, attr_dict)
        return func


class PymongoCollection(BaseCollection):
    ops = ['drop', 'create_indexes', 'insert', 'find']

    def __init__(self, db):
        self.db = db

    @classmethod
    def ensure_unique(cls):
        indexes = []
        for item in cls.__unique_index__:
            indexes.append(IndexModel(item, unique=True, background=True))
        res = cls.create_indexes(indexes)
        return res

    def commit(self):
        data = self.dump()
        self.__class__.insert(data)


class MotorCollection(BaseCollection):
    ops = ['find']

    def __init__(self, db):
        self.db = db

    # @classmethod
    # def ensure_unique(cls):
    #     indexes = []
    #     for item in cls.__unique_index__:
    #         indexes.append(IndexModel(item, unique=True, background=True))
    #     res = cls.create_indexes(indexes)
    #     return res

    # def commit(self):
    #     data = self.dump()
    #     self.__class__.insert(data)

