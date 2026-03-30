nMonths = int(input())
kRabbitPairs = int(input())




"""


            1 2 3 4 5

total:      1 1 4 7 19
breedable:  0 1 1 4


**** LOOP AND HOLD VALUE OF PREVIOUS MONTH to multiply by



"""

monthlyPattern = []
nowAgedRabbits = 0
totalRabbits = 1


for i in range (0, nMonths - 1):
    if i == 0:
        monthlyPattern.append(1)
        nowAgedRabbits = 1
    if i == 1:
        monthlyPattern.append(1)
        pass
    else:
        totalRabbits = (nowAgedRabbits * kRabbitPairs) + totalRabbits
        monthlyPattern.append(totalRabbits)
        nowAgedRabbits = totalRabbits - (nowAgedRabbits * kRabbitPairs)




print(monthlyPattern)

    
    
    