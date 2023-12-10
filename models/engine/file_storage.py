#!/usr/bin/python3
"""
Module for FileStorage class.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class for serialization and deserialization.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                dict_objs = json.load(file)
                for key, value in dict_objs.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)
                    new_obj = cls(**value)
                    FileStorage.__objects[key] = new_obj
        except FileNotFoundError:
            pass
