str1 = "Listen"
str2 = "Silent"
str1 = str1.replace(" ", "").upper()
str2 = str2.replace(" ", "").upper()
print(sorted(str2))
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not an Anagram")