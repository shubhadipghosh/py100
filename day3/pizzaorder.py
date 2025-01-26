print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size == "L":
    pepperoni_status = "without pepperoni"
    extra_cheese_status = "without extra cheese."
    price = 25
    if pepperoni == "Y":
        price += 3
        pepperoni_status = "with pepperoni"
    if extra_cheese == "Y":
        price += 1
        extra_cheese_status = "with extra cheese."
    print("You have ordered Large pizza "+pepperoni_status + " and "+extra_cheese_status+"\n"+"The total bill is: ", price)
elif size == "M":
    pepperoni_status = "without pepperoni"
    extra_cheese_status = "without extra cheese."
    price = 20
    if pepperoni == "Y":
        price += 3
        pepperoni_status = "with pepperoni"
    if extra_cheese == "Y":
        price += 1
        extra_cheese_status = "with extra cheese."
    print(
        "You have ordered Medium pizza " + pepperoni_status + " and " + extra_cheese_status + "\n" + "The total bill is: ",
        price)
else:
    pepperoni_status = "without pepperoni"
    extra_cheese_status = "without extra cheese."
    price = 15
    if pepperoni == "Y":
        price += 2
        pepperoni_status = "with pepperoni"
    if extra_cheese == "Y":
        price += 1
        extra_cheese_status = "with extra cheese."
    print(
        "You have ordered Small pizza " + pepperoni_status + " and " + extra_cheese_status + "\n" + "The total bill is: ",
        price)