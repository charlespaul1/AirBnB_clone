#!/usr/bin/python3

"""
defining the basemodel of the console,
it has common attributes for other classes
"""
import sys
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    base class for other classes used in the console
    """
    def __init__(self, *args, **kwargs):
        """
        initialitizing public instance attributes
        (id, created_at, updated_at)
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")

            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """
            returning a string representation of the BaseModel
        """
        return("[{}], ({}), {}".format(self.__class__.__name__,
                                       self.id, self.__dict__))

    def __repr__(self):
        """
        returning a string representation of the BaseModel
        """
        return("[{}], ({}), {}".format(self.__class__.__name__,
                                       self.id, self.__dict__))

    def save(self):
        """
        updates the updated_at attribute with new
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
         returns a dictionary containing all keys/values of
         __dict__ of the instance:
        """
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = self.__class__.__name__
        cp_dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cp_dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return cp_dct
