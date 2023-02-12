#!/usr/bin/python3
"""
Unittest FileStorage class
"""
import unittest
import os
from models import base_model
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestDocsB(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)


class BaseModelclassTests(unittest.TestCase):
    """ Test Case for base_model moudle """

    def setUp(self):
        """ Create instance global  """
        self.ins0 = FileStorage()
        self.ins1 = FileStorage()

    def tearDown(self):
        """ Clean All test case """
        pass

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(exe)

    def test_isinstance(self):
        """ Test if a variable is instance of FileStorage """
        self.assertIsInstance(self.ins0, FileStorage)

    def test_all(self):
        """ The dict return is a dictionary """
        dic = self.ins0.all()
        self.assertEqual(type(dic), dict)
        self.assertIs(dic, self.ins0._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
