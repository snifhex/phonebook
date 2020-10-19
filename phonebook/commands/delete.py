from store import Store


class DeleteContact(object):
    def __init__(self):
        self.store = Store
        self.database = self.store.load()

    def delete(self, phoneNumber):
        del self.database[phoneNumber]
        self.store.save(self.database)


Del = DeleteContact()

# Del.delete(99292992)
