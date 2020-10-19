from store import Store


class AddContact():
    def __init__(self):
        self.store = Store
        self.database = self.store.load()

    def create(self, name, phoneNumber, address):
        if not phoneNumber in self.database:
            self.database[phoneNumber] = {"name": name, "address": address}
            self.store.save(self.database)

    def forcedUpdate(self, name, phoneNumber, address):
        self.database[phoneNumber] = {"name": name, "address": address}
        self.store.save(self.database)


Add = AddContact()
# Add.create("sa", 99292992, 'addres something shit')
