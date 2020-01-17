# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room_key, items):
        self.name = name
        self.room_key = room_key
        self.items = items

    def get_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to your inventory")


    def drop_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Dropped {item.name}")
        else:
            print("You don't have that item.")