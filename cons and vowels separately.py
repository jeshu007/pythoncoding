def separate_vowels_consonants(string):
    vowels = "AEIOUaeiou"
    vowels_list = []
    consonants_list = []
    for char in string:
        if char in vowels:
            vowels_list.append(char)
        elif char.isalpha():
            consonants_list.append(char)

    return vowels_list, consonants_list

string = input("Enter a string: ")
vowels, consonants = separate_vowels_consonants(string)
print("Vowels:", "".join(vowels))
print("Consonants:", "".join(consonants))
