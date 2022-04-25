# Working with strings

phrase = "I said: "

# New line
print("Hello \nworld")

# Inserting quotation marks in strings
print("Hello \"world\"")

# Concatenation
print(phrase + "Hello world")

# upper case / lower case
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())

# length of string
print(len(phrase))

# first letter of phrase
print(phrase[0])

# first index of ___
print(phrase.index("a"))
print(phrase.index("said"))

# replacing words
print(phrase.replace("said", "shouted"))
