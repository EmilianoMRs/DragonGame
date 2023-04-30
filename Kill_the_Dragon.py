import random
print("you have enter a dungeon and spotted a dragon far away")
correr_o_quedarse = int(input("--will you run or stay 'press 1'to run 'press 2' to stay = "))
if correr_o_quedarse == 1:
    vives_o_mueres = random.randint(0,1)
    if vives_o_mueres == 1:
        print('you will live, this is not the expected ending💖')
    elif vives_o_mueres == 0:
        print('the dragon have burned your,Game Over💔')

