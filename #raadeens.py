#raadeens
from math import radians
import random
score = 0
for i in range(0,20):
    random_number = random.randint(1,1000)
    for i in range(0,10):
        print ('type een cijfer hoger dan 1000 om te stoppen\n')

        geradengetal = int(input ('Kies een nummer tussen de 1 en 1000: '))
        
        if geradengetal > 1000:
            exit()
        
        elif geradengetal == (random_number):
            print('Goed gedaan')
            score = score + 1
            print ('Jouw score is: '+ str(score))
            break

        elif geradengetal < (random_number):
            print ('Je moet hoger schatten')

            if geradengetal > random_number-20 and geradengetal < random_number+20:
               
                print('je bent heel warm')
            elif geradengetal > random_number-50 and geradengetal < random_number+50:
                print('je bent warm')

        elif geradengetal > (random_number):
            print ('Je moet lager schatten')

            if geradengetal > random_number-20 and geradengetal < random_number+20:
                print('je bent heel warm')

            elif geradengetal > random_number-50 and geradengetal < random_number+50:
                print('je bent warm')

        
    print ('\n---------------->nieuw getal is gekozen<----------------')
    