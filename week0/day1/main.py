print("start week 0 day 1")

'''
Mini exercises:
Ask user for their name and age
Print how old they’ll be in 5 years
Make a loop that prints numbers 1–10
Store 5 foods in a list and print them one by one
Create a function called greet(name)
'''
# Ask user for their name and age
name = input("Hello, User! what is your name? ")
age = int(input("How old are you? "))

# Print how old they’ll be in 5 years
age_in_five = (f"This is how old you`ll be in 5 years: {age + 5}")
print(age_in_five)

# Make a loop that prints numbers 1–10
for n in range(1,11):
    print (n)

# Store 5 foods in a list and print them one by one
foods = ["tofu","broccoli","rice","soy","pepper"]
for food in foods:
    print(food)

# Create a function called greet(name)
def greet(name):
    greeting = "Hello " + name + "!"
    return greeting
print(greet("JJ"))