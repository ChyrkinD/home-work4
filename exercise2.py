import random

def get_numbers_ticket(min, max, quantity):
    result = set()
    if(min < 0 or max > 1000):
        return result
    
    
    while(quantity > 0):
        number = random.randint(min,max)

        while number in result:
            number = random.randint(min,max)
        result.add(number)

        quantity -=1
    
    return result
    

print(get_numbers_ticket(1,20,5))