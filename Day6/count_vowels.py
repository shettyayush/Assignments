def count_vowels(s):
    vowels = "aeiou"
    c = 0
    for ch in s.lower():
        if ch in vowels:
            c += 1
    return c

j = input("Enter a string: ")
print(count_vowels(j))
