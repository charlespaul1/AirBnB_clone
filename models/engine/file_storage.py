#!/usr/bin/python3
"""
file storage
"""
import json
import models


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):

        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        obj : An instance object
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        objects_dict = {}
        for key, value in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
