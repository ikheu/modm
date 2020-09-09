class ModmException(Exception):
    """ base exception of modm """


class FieldInvalid(ModmException):
    """ when filed is invalid """

class FieldLacked(ModmException):
    """ when filed is not enough """
