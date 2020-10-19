from store import Store


class SearchContact(object):
    def __init__(self):
        self.store = Store
        self.database = self.store.load()

    def search(self, phoneNumber=None, name=None, address=None):
        if phoneNumber and name and address:
            data = self.database[phoneNumber]
            print(
                f"Name : {data['name']}\nPhone Number : {phoneNumber}\nAddress : {data['address']}")
        elif phoneNumber:
            data = self.database[phoneNumber]
            print(
                f"Name : {data['name']}\nPhone Number : {phoneNumber}\nAddress : {data['address']}")


Search = SearchContact()
