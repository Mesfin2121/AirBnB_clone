#!/use/bin/python3

import json
from models.base_model import BaseModel


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__
        FileStorage.__objects['{}.{}'.format(class_name, obj.id)] = obj

    def save(self):
        path = FileStorage.__file_path
        object_dict = FileStorage.__objects
        object_dict2 = {
            obj: object_dict[obj].to_dict() for obj in object_dict.keys()
        }

        with open(path, 'w') as f:
            json.dump(object_dict2, f)

    def reload(self):
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
