                                    # Try It Yourself!

"""
Try these short programs to get some firsthand experience with Python’s lists.
You might want to create a new folder for each chapter’s exercises to keep 
them organized.
"""

"""
3-1. Names: Store the names of a few of your friends in a list called names. Print 
each person’s name by accessing each element in the list, one at a time.
"""
names = ["Ana","Berta","Carlos","Diana","Erick","fabian","gustaVO"]
print(names)
print(names[0],names[1],names[2],names[3], names[4],names[5],names[-1])


"""
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the 
person’s name.
"""
greetings ="hola,"
print(greetings ,names[0].title())
print(greetings,names[-1].title())

"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a 
motorcycle or a car, and make a list that stores several examples. Use your list 
to print a series of statements about these items, such as “I would like to own a 
Honda motorcycle.
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print ("I would like to own a ",bicycles[1])