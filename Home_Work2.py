from random import randint

result = set()

#Creat func for lottery tickets numbers
def get_numbers_ticket(min, max, quantity):
    while len(result) != quantity:
        result.add(randint(min, max))
    sorted_result = sorted(list(result))
    return sorted_result

print(get_numbers_ticket(1, 40, 5))
