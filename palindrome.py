# Check if a given string is a palindrome

word = input("Enter any word: ")

# Reverse the word
reversed_word = word[::-1]

# Check if the original word is equal to the reversed word
if word == reversed_word:
    print(f"Your word '{word}' is a palindrome.")
else:
    print(f"Your word '{word}' is not a palindrome.")
