output = "{} is {} years old. He is an {}."
print(output.format("Nick", 59, "engineer"))

name = "John"
age = 56
# 'f-strings' get their name, nad it tells Python that we want to format the following string.
print(f"{name} is {age * 12} months old.")

# Basic String Processing
# .lower , .upper, .capitalize, .title
print("Hello World".capitalize())

# .strip()
print("Hello World    ".strip())
#
#
greeting = "Hello, world"
mark = "!"
print(f"{greeting}{mark}")
#
"""
name = input("enter your name: ").strip().title()
print(f"Hello, {name}!") """
#
output = "{} {}"
print(output.format("I am", 29))

#
#output = "{} ({}), directed by {}"

title = "Joker"
director = "Todd Phillips"
release_yr = 2019
output = "{} ({}), directed by {}"
print(output.format(title, release_yr, director))