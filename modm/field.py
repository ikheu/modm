import abc


class Descriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.real_attr)

    def __set__(self, instance, value):
        setattr(instance, self.real_attr, value)


class BaseField(abc.ABC, Descriptor):
    def __init__(self, unique=False, require=True, **kwargs):
        self.unique = unique
        self.require = require
        if not self.require and 'default' in kwargs:
            self.default = kwargs['default']
    
    def __set__(self, instance, value):
        if hasattr(self, 'default') and self.default is None and value is None:
            pass
        else:
            value = self.validate(value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, value):
        """return validated value or raise ValueError"""


class TypeField(BaseField):
    def validate(self, value):
        if isinstance(value, self.allow_type):
            return value
        else:
            raise ValueError(" ")


class StrField(TypeField):
    allow_type = str
    

class IntField(TypeField):
    allow_type = int


class DictField(TypeField):
    allow_type = dict


class ListField(TypeField):
    allow_type = list


class BoolField(TypeError):
    allow_type = bool


class DateField(BaseField):
    def validate(self, value):
        return value
