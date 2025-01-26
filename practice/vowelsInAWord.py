vowels = ['a', 'e', 'i', 'o', 'u']
wordOne = "cauliflower"
wordTwo = "programming"


def countVowels(word: str, vowels: list = vowels):
    count = 0
    for c in word:
        if c in vowels:
            count += 1
    return word + " contains " + str(count) + " vowels"


print(countVowels(wordOne))

print(countVowels(wordTwo))
