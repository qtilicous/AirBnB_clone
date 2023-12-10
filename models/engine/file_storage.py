#!/usr/bin/python3
"""
Module for FileStorage class
"""

import json
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)

            for key, obj_data in obj_dict.items():
                class_name, obj_id = key.split('.')
                obj_data['created_at'] = datetime.strptime(obj_data['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                obj_data['updated_at'] = datetime.strptime(obj_data['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                obj = eval(class_name)(**obj_data)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass


# If the script is run directly, execute the sample test
if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()

    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)
