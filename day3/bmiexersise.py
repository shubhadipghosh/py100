weight = 70
height = 1.85

bmi = weight / (height ** 2)
print(bmi)
# 🚨 Do not modify the values above
# Write your code below 👇
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")
