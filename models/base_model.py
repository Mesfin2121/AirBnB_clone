#!/usr/bin/python3
"""
Define base or parent class for all classes in this project.
"""

import models
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """Define all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a Basemodel object instances

        Args:
            *args (): We don't use this argument
            **kwargs (dict): It's dict and it's key is an instances
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"

            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """Represent class instances."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Save changes and updates"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        dict_cpy = self.__dict__.copy()
        dict_cpy['id'] = self.id
        dict_cpy['created_at'] = self.created_at.isoformat()
        dict_cpy['updated_at'] = self.updated_at.isoformat()
        dict_cpy['__class__'] = self.__class__.__name__
        return dict_cpy
