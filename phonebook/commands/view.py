from store import Store


class ViewContact(object):
    def __init__(self):
        self.store = Store
        self.database = self.store.load()

    def view(self):
        for key in self.database.keys():
            data = self.database[key]

            print(
                f"Name : {data['name']}\nPhone Number : {key}\nAddress : {data['address']}")


View = ViewContact()
# View.view()
