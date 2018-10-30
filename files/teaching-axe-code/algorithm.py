import random

def decideToBuyOrSell(price):
    if(random.randint(0,100) % 4 == 1):
        return 'buy'
    elif(random.randint(0,100) % 25 == 0):
        return 'sell'
    return ''
