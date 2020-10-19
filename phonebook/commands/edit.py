from store import Store


class EditContact(object):
    def __init__(self):
        self.store = Store
        self.database = self.store.load()

    def edit(self, phoneNumber, name=None, address=None):
        if name and address:
            self.database[phoneNumber] = {"name": name, "address": address}
        elif name:
            self.database[phoneNumber]["name"] = name
        elif address:
            self.database[phoneNumber]["address"] = address
        self.store.save(self.database)


Edit = EditContact()

# Edit.edit(99292992, name='sachin', address="yolo")
