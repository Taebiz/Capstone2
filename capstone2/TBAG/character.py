#SUPER CLASS
class Character():
#Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    
    #Describe this character
    def describe (self):
        print (f'{self.name} is here!')
        print( self.description )

    #What this charact will say when talked to
    def set_conversation (self, conversation):
        self.conversation = conversation
    
    #Talk to this character
    def talk(self):
        if self.conversation is not None:
            print(f'[{self.name} says:]: {self.conversation}')
        else:
            print(f'{self.name} does not want to talk to you.')

    def fight(self, combat_item):
            print(f'{self.name} does not want to fight you.')
            return True

#Sub Class
class Enemy (Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.sleeping = False  #Task 3
    
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness
    
    def get_weakness(self):
        return self.weakness
    
    #Task 3    
    def send_to_sleep(self):
            self.sleeping = True
            print(f'{self.name} falls asleep')

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f'You fend {self.name} off with the {combat_item}')
            return True
        else:
            print(f'Your {combat_item} is useless')
            print(f'{self.name} crushes you, puny adventurer')
            print('GAME OVER')#Task 2
            return False
   
   
#Task 4
class Friend (Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.give_gift = None



        

