import os
import pickle

FILENAME = 'phonebook.pickle'


class StorageClass(object):
    def __init__(self):
        self.fname = FILENAME
        if not self.check():
            self.create()

    def check(self):
        if os.path.exists(self.fname):
            return True
        else:
            return False

    def create(self):
        database = dict()
        with open(self.fname, "wb") as file_obj:
            pickle.dump(database, file_obj)

    def load(self):
        with open(self.fname, "rb") as file_obj:
            database = pickle.load(file_obj)
        return database

    def save(self, database):
        with open(self.fname, "wb") as file_obj:
            pickle.dump(database, file_obj)


Store = StorageClass()
