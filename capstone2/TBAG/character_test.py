from character import Enemy


dave = Enemy('Dave', 'A smelly zombie') # creating a new instance
dave.describe()

dave.set_conversation('braaaainnnsss')
dave.talk()

dave.set_weakness('cheese')

send_to_sleep = input('Do you want to send Dave to sleep? (yes/no): ')#Task 3
if send_to_sleep.lower() == 'yes':
    dave.send_to_sleep()
else:
    weapon = input('What will you fight with > ')
    dave.fight(weapon)





