class Room():
    def __init__(self, room_name):#creating a constructor.if creating an attribute you need to do it on the self object.
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None # aggregation - ability to contain a character

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name
    
    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):

        print(self.name)
        print('----------------')
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print('The ' + room.get_name()+ ' is '+ direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print('You can\'t go that way')
            return self
    
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    
