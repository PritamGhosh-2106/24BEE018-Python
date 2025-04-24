import random
def generate_random_numbers():
    return random.sample(range(-15, 16), 10)
def square_numbers(numbers):
    return [num ** 2 for num in numbers]

random_numbers = generate_random_numbers()  
squared_numbers = square_numbers(random_numbers)  

print("Original List of Random Numbers:", random_numbers)
print("List of Squared Numbers:", squared_numbers)
