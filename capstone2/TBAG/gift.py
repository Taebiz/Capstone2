class gift():
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
        