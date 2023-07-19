vowels={'a','e','i','o','u'}
x=input().lower()
not_vowels=[i for i in x if i not in vowels]
print(not_vowels)