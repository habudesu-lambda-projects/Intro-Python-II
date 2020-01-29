# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def item_taken(self, item):
        self.items.remove(item)

    def item_dropped(self, item):
        self.items.append(item)