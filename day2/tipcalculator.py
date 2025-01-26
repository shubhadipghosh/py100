print("========Welcome to the Top Calculator===============")
total_bill = float(input("What was the total bill? $"))
tips_wants_to_give = int(input("How much tip would you like to give? $10, $12 or $15? $"))
number_of_people = int(input("How many people to split the bill? ") )
each_person_pay = ((total_bill+tips_wants_to_give)/number_of_people)

print("Each person should pay $"+str("%.2f" %each_person_pay))
