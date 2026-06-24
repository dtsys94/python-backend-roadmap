# collect user data
bill_amount = float(input("Bill amount: "))
tip_percentage = int(input("Tip percentage: "))
people_number = int(input("Amount of people: "))

# defyne functions
def calculate_tip(bill_amount, tip_percentage):
    tip_amount = bill_amount / 100 * tip_percentage
    return tip_amount

def calculate_total(bill_amount, tip_amount):
    total_price = bill_amount + tip_amount
    return total_price

def calculate_per_person(total_price, people_number):
    per_person = total_price / people_number
    return per_person

#call functions and save the result
tip_amount = calculate_tip(bill_amount, tip_percentage)
total_bill = calculate_total(bill_amount, tip_amount)
amount_per_person = calculate_per_person(total_bill, people_number)

print(f"Tip Amount: {tip_amount}")
print(f"Total Bill: {total_bill}")
print(f"Amount Per Person: {amount_per_person}")
