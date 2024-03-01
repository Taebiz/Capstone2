from character import Friend 

zack = Friend('Zack', 'A brave kid')
zack.describe()
zack.give_gift()
zack.set_conversation('I think you\'re just having a bad day.')
zack.talk()



give_gift = input('Do you want to give Zack a gift? (yes/no): ')#Task 4
if give_gift.lower() == 'yes':
    zack.give_gift()