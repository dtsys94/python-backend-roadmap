# check if number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(5))
print(is_even(10))

# find the largest number
def find_largest(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest

print(find_largest([5, 10, 3, 8]))

# calculate tax
def calculate_tax(price):
    tax = price * 0.08
    total = price + tax
    return round(total, 2)

print (calculate_tax(100))
print (calculate_tax(134))
print (calculate_tax(0.99))

# default parameters
def greet(name="Friend"):
    return f"Hello {name}"

print(greet())
print(greet("JJ"))

def love(name="baby"):
    return f"I love you, {name}"

print(love())
print(love("JJ"))

def calculate_discount(price, discount_percent):
    return price - price * discount_percent / 100

print(calculate_discount(100,20))
print(calculate_discount(34,5))