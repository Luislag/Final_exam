import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        random_numbers[i] = random.randint(20, 30)
    elif random_numbers[i] < 50:
        random_numbers[i] = "XX"
print(random_numbers)