from room import Room
from character import Enemy
from character import Friend
from item import item
from gift import gift


print('Welcome to the Bootcamp Test Base Adventure Game! (BTBAG)')
kitchen = Room('kitchen')
ballroom = Room('Ballroom')
dining_hall = Room('Dining Hall')
item = Room('kitchen')

kitchen.set_description('A dank and dirty room buzzing with files')
ballroom.set_description('A decaiyng ballroom with an old wooden floor')
dining_hall.set_description('A dining room frozen in time with cracked wallpaper')
item.set_description('A heavy and precious sword')


kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

dave = Enemy('Dave', 'A smelly zombie')
dave.set_conversation('Braaaaaaaaainnnsssssss')
dave.set_weakness('cheese')
dining_hall.set_character(dave)

zack = Friend('Zack', 'A brave kid')
zack.set_conversation('I\'m here to save the day!')
zack.set_weakness('smelly breath')
ballroom.set_character(zack)

gift.set_description('An old but shiny key')


current_room = ()
while True:
    print()
    current_room.get_details()

    inhabitant = current_room.get_character()

    if inhabitant is not None:
        inhabitant.describe()

    command = input('What is your command> ')
    if command in ['north', 'south', 'east', 'west']:
        current_room == current_room.move(command)
    elif command == 'talk':
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print('There is no one to talk to here..!')   
    elif command == 'exit':
        break
    
    current_room = current_room.move(command)







        
