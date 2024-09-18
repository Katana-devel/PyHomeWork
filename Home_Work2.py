from random import randint

#Creat func for lottery tickets numbers
def get_numbers_ticket(min, max, quantity):
    result = set()
    try:
        while len(result) != quantity:
            result.add(randint(min, max))
    except ValueError:
        return []
    sorted_result = sorted(list(result))
    return sorted_result

print(get_numbers_ticket(10, 4, 5))
