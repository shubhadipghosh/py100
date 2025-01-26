import random
friends_list = ["Allice", "Bob", "Charlie", "David", "Emanuel"]

# 1sy way
print("Bill will be paid by: "+ random.choice(friends_list))

# 2nd way
# random_payer = random.randint(0, len(friends_list)-1)
# print(random_payer)
# print("Bill will be paid by: ", friends_list[random_payer])