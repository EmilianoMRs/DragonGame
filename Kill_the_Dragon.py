import random
print("you have enter a dungeon and spotted a dragon far away")
run_or_stay = int(input("--will you run or stay 'press 1'to run 'press 2' to stay = "))
if run_or_stay == 1:
    live_or_die = random.randint(0,1)
    if live_or_die == 1:
        print('you will live, this is not the expected ending💖')
    elif live_or_die == 0:
        print('the dragon have burned your,Game Over💔')
if run_or_stay == 2:
    print("the game starts")
    armor = ("dimon", "gold", "silver")
    weapons = ("bow", "sword", "magic staff")
    print ("you have found a set of armors and wapons that are compose by" , armor , 'and' , weapons)

