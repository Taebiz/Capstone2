# #The item class should have:
# Attributes for the name and the descript of the item - a sword
# a constructor method
# getters and setters for the name and the description of the item
# any additional attributes and methods that you would like


class item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
    
    def set_description(self, new_description):
        self.description = new_description

    def describe(self):
        print(self.description)
        
