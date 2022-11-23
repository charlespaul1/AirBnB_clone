#!/usr/bin/python3

"""
defining the basemodel of the console,  it has common attributes for other classes
"""
import uuid
from datetime import datetime
import models

class Basemodel:
    """
    base class for other classes used in the console
    """
    def __init__(self, *args, **kwargs):
        """
        initialitizing public instance attributes(id, created_at, updated_at)
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())#unique id
            self.created_at = datetime.now()# datetime when is created
            self.updated_at  = datetime.now() # date when is updated
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)
    def __str__(self):
        """
        returning a string representation of the basemodel
        """
        return("[{}], ({}), {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def __repr__(self):
        """
        returning a string representation of the basemodel
        """
        return("[{}], ({}), {}".format(self.__class__.__name__, self.id, self.__dict__))
    def save(self):
        """
        updates the updated_at attribute with new
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns dictionary representation of the basemodel class
        """
        dict_copy = dict(self.__dict__)
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict_copy['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return dict_copy




