#!/use/bin/python3
"""
Defines the FileStorage class which used to interact with json file.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class FileStorage():
    """
    Storage engine
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all current objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set class name and id to each new key"""
        class_name = obj.__class__.__name__
        FileStorage.__objects['{}.{}'.format(class_name, obj.id)] = obj

    def save(self):
        """Write(serialize) the object to a json file."""
        path = FileStorage.__file_path
        object_dict = FileStorage.__objects
        object_dict2 = {
            obj: object_dict[obj].to_dict() for obj in object_dict.keys()
        }

        with open(path, 'w') as f:
            json.dump(object_dict2, f)

    def reload(self):
        """Read(deserilize) the object from a json file."""
        path = FileStorage.__file_path
        try:
            with open(path) as f:
                load_object = json.load(f)
                for obj in load_object.values():
                    cls_name = obj['__class__']
                    del obj['__class__']
                    self.new(eval(cls_name)(**obj))
        except Exception:
            pass
