
##  use quotes and apostrophes

print('I told my friend, "Python is my favorite language!"')
print("The language 'Python' is named after Monty Python, not the snake.")
print("One of Python's strengths is its diverse and supportive community.")

## Changing Case in a String with Methods

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

## Combining or Concatenating Strings

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

## Adding Whitespace to Strings with Tabs or Newlines

print("Python") 
print("\tPython") #To add a tab to your text, use the character combination \t
print("\npython") # to add a newline in a string, use the character combination \n


## Stripping Whitespace
favorite_language = 'python ' 
favorite_language.rstrip() # this remove temporaly rigth side
print( 'python' == favorite_language) # demostrate is temporal removed
favorite_language = favorite_language.rstrip() # removed permanently only storing the value again

favorite_language = ' python'
print(favorite_language.lstrip()) # remove left side

favorite_language = ' python '
print(favorite_language.strip()) # remove both side



## AVOIDING SINTAX Error

message = "One of Python's strengths is its diverse community." 
print(message)

"""
but if you use one ' quotes python does not how to interptretate

message = 'One of Python's strengths is its diverse community.'
print(message)
"""