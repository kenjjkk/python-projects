print("  !!!!!!!welcome to ken's pizzahut!!!!!!")

pizza = ['1. napoletana','2. rustica','3. capricciosa']
for i in pizza:
        print(i)

pizzachoice = int(input("choose your pizza: "))

if pizzachoice == 1:
    print('pizza napoletana, wait 7min')
elif pizzachoice == 2:
    print('pizza rystica, wait 10min')
elif pizzachoice == 3:
    print('pizza capricciosa, wait 15min only!!')

else:
    print('nun of the pizzas, gimme coke')
