numberList = [12, 3, 55, 23, 6, 78, 33, 4]
min = numberList[0]
max = numberList[0]
for num in numberList:
    if num < min:
        min = num
    if num > max:
        max = num
print(f"Minimum number is {min} and Maximum number is {max}")


