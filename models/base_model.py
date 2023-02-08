#!/usr/bin/python3

import models
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """
    """

    def __init__(self, *args, **kwargs):

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
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        dict_cpy = self.__dict__.copy()
        dict_cpy['id'] = self.id
        dict_cpy['created_at'] = self.created_at.isoformat()
        dict_cpy['updated_at'] = self.updated_at.isoformat()
        dict_cpy['__class__'] = self.__class__.__name__
        return dict_cpy
