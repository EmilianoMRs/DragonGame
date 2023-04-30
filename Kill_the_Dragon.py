import random
print("--haz entrado en una masmorra y vez un dragon a lo lejos")
correr_o_quedarse = int(input("--te quedatas o correras = preciona 'preciona 1'corres 'preciona 2' te quedas"))
if correr_o_quedarse == 1:
    vives_o_mueres = random.randint(0,1)
    if vives_o_mueres == 1:
        print('vives,no es un fin pero es algo💖')
    elif vives_o_mueres == 0:
        print('muerto el dragon te a quemado,fin del juego💔')

