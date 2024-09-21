
def notnegat(input):
    numb = float(input)
    if numb < 0:
        print('Помилка, введіть число більше за 0')
        quit()
    elif numb == 0:
        print('Помилка, введіть число більше за 0')
        quit()
    return numb
    

import math
#Довжина кола
C = float(notnegat(input('Довжина кола:')))

#Радіус
r = C / (2* math.pi)

#Площа кола
S = math.pi * r**2

print("Площа кола:", S)