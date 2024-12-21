#!/usr/bin/env python
# coding: utf-8


from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32806
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# method to implement the C in CRUD.
    
    def create(self, data):
        if data is not None:
            insertSuccess = self.database.animals.insert_one(data)  
            if insertSuccess != 0: 
                return False
            return True #
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# method to implement the R in CRUD.

    def read(self, searchData):
        if searchData:
            data = self.database.animals.find(searchData, {"_id": False})
        else: 
            data = self.database.animals.find( {}, {"_id": False})
        return data

# method to implement the U in CRUD

    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.databse.animals.update_many(searchData, {"$set": updateData})
        else:
            return "{}"
        return result.raw_result

# method to implement the D in CRUD
    
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else: 
            return "{}"
        return result.raw_result





