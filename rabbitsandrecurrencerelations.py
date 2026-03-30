nMonths = int(input())
kRabbitPairs = int(input())

"""The population begins in the first month with a pair of newborn rabbits.

Rabbits reach reproductive age after one month.

In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.

Exactly one month after two rabbits mate, they produce one male and one female rabbit.

Rabbits never die or stop reproducing."""

"""
1. collect number of months (n) and number of rabbit pairs
2. iterate over length of months
3. account for amount of pairs able to reproduce"""

"""


1 2 3 4 5

1 4 8 19



**** LOOP AND HOLD VALUE OF PREVIOUS MONTH to multiply by



"""
monthlyPattern = []
nowAgedRabbits = 0


for i in range (0, nMonths):
    if i == 0:
        monthlyPattern.append(1)
        nowAgedRabbits = 1

    
    
    