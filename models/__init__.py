#!/usr/bin/python3
"""Models() is module which contain
    -User
    -City
    -State
    -Amenity
    -Place
    -Review classes.
Usage:
    import models
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
