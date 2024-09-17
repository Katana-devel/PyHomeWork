from random import randint

result = set()

#Creat func for lottery tickets numbers
def get_numbers_ticket(min, max, quantity):
    while len(result) != quantity:
        result.add(randint(min, max))
    return print(sorted(list(result)))

get_numbers_ticket(1, 40, 5)