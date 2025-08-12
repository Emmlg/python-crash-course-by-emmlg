#                                Try It Yourself
"""
3-8. Seeing the World: Think of at least five places in the world you’d like to 
visit.
•	 Store the locations in a list. Make sure the list is not in alphabetical order.
•	 Print your list in its original order. Don’t worry about printing the list neatly, 
just print it as a raw Python list.
•	 Use sorted() to print your list in alphabetical order without modifying the 
actual list.
•	 Show that your list is still in its original order by printing it.
•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
•	 Show that your list is still in its original order by printing it again.
•	 Use reverse() to change the order of your list. Print the list to show that its 
order has changed.
•	 Use reverse() to change the order of your list again. Print the list to show 
it’s back to its original order.
•	 Use sort() to change your list so it’s stored in alphabetical order. Print the 
list to show that its order has been changed.
•	 Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed
"""

country_future_visit = ["united state", "singapur","france","israel","russia","japan"]
print(country_future_visit)

print(sorted(country_future_visit))
print("original order : ",country_future_visit)
country_future_visit.reverse()
print(country_future_visit)


country_future_visit.sort(reverse=True)
print("permanently sorted reverse :" ,country_future_visit)


"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
through 3-7 (page 46), use len() to print a message indicating the number 
of people you are inviting to dinner.
"""
guest_list = ["abigail","Eduardo","Carlos"]
print(f"the length of guest list is : {len(guest_list)}")

"""
3-10. Every Function: Think of something you could store in a list. For example, 
you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items 
and then uses each function introduced in this chapter at least once.

"""
most_speaking_lang = [
  "chino","Hindi","Español", "Árabe", "Francés",
  "Bengalí","Ruso","Portugués","Urdu","Indonesio"
]

# Creating, adding
most_speaking_lang[1] = most_speaking_lang[1] + "Mandarín"
print("original list :",most_speaking_lang)
most_speaking_lang.insert(0, "Inglés")
most_speaking_lang.insert(2,"Español")
most_speaking_lang.append("Alemán")

# reading
print(f"after adding : {most_speaking_lang}")

# removing

del most_speaking_lang[3]
del most_speaking_lang[8]
most_speaking_lang.pop()
print("pop ()",most_speaking_lang)
most_speaking_lang.remove("Ruso")

print("after removing : ",most_speaking_lang)

# organizing:

print("temporal ASC" , sorted(most_speaking_lang))
print ("temporal DESC ",sorted(most_speaking_lang,reverse=True))

most_speaking_lang.sort()
print(f"permantanly sort ",most_speaking_lang)

most_speaking_lang.reverse()
print("revert a list : ",most_speaking_lang)

print( "applied sort : ",most_speaking_lang.sort()) # nothing to show due to is void method
print(most_speaking_lang)

print(f"final list sizes: {len(most_speaking_lang)}")