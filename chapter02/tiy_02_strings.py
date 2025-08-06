
                                    # Try It Yourself!
# 2-3.
"""
2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric, 
would you like to learn some Python today?”
"""
random_name = "emmlg"
print("hello "+random_name +"\nwould you like to learn some Python today?")

#2-4.
"""
2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.
"""
naming_name = "Eric"
print(naming_name.lower())
print(naming_name.upper())
print(naming_name.title())

#2-5.
"""
2-5. Famous Quote: Find a quote from a famous person you admire. Print the 
quote and the name of its author. Your output should look something like the 
following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
"""
print('Apostle paul once said \n"I am crucified with Christ: \nnevertheless I live; yet not I, but Christ liveth in me: \nand the life which I now live in the flesh \nI live by the faith of the Son of God, who loved me, and gave himself for me."')

#2-6.
"""
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous person’s name in a variable called famous_person. Then compose your message 
and store it in a new variable called message. Print your message.
"""
famouse_person = "Apostle paul"
phrase = '"I am crucified with Christ: \nnevertheless I live; yet not I, but Christ liveth in me: \nand the life which I now live in the flesh \nI live by the faith of the Son of God, who loved me, and gave himself for me."'
message = famouse_person + phrase
print(message)

#2-7.
"""
2-7. Stripping Names: Store a person’s name, and include some whitespace 
characters at the beginning and end of the name. Make sure you use each 
character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(), 
rstrip(), and strip()
"""

original_name = "\t  José María Teclo Morelos Pavón y Pérez. Es más conocido como José María Morelos y Pavón   "
print("temporal removed R: "+ original_name.rstrip())
print("temporal removed L: "+ original_name.lstrip())
original_name = original_name.strip()
print(original_name)
print("Nombre completo : \n"+original_name)
