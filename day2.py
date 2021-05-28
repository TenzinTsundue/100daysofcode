#Tip calculator
#total bill, tip percentage, how many people 
#each person should pay as an out put

total_amount = float(input("what is the total bill: "))
discount_percent = int(input("what % of tip you want to give eg:10, 15, 20? "))
no_of_people = int(input("how many people to split the bill : "))

total_payable = total_amount + total_amount *discount_percent/100

payable_per_person = round(total_payable/no_of_people, 2)

print(f"Each person should pay ${payable_per_person} ") 