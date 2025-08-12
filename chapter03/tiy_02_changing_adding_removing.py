#                                     Try It Yourself
"""
The following exercises are a bit more complex than those in Chapter 2, but 
they give you an opportunity to use lists in all of the ways described.
"""

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
#would you invite? Make a list that includes at least three people you’d like to 
#invite to dinner. Then use your list to print a message to each person, inviting 
#hem to dinner

guest_list = ["abigail","Eduardo","Carlos"]
print(f"bienvenido , {guest_list[0]}")
print(f"bienvenido , {guest_list[1]}")
print(f"bienvenido , {guest_list[-1]}")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the 
# dinner, so you need to send out a new set of invitations. You’ll have to think of 
# someone else to invite.
# •     Start with your program from Exercise 3-4. Add a print statement at the 
#       end of your program stating the name of the guest who can’t make it.
# •     Modify your list, replacing the name of the guest who can’t make it with 
#       the name of the new person you are inviting.
# •     Print a second set of invitation messages, one for each person who is still in your list.

print(guest_list)
print("the person who can't make it is : ",guest_list[1])
guest_list[1] = "Erick"
print("new list is : ",guest_list)
print("welcome to dinner : ",guest_list[0],guest_list[1],guest_list[2])


# 3-6. More Guests: You just found a bigger dinner table, so now more space is 
# available. Think of three more guests to invite to dinner.
# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a 
# bigger dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list.

print("guest what? , we found new guest.")
guest_list.insert(len(guest_list)//2,"Daniel")
guest_list.insert(0,"Fabian")
guest_list.insert(-1,"Gabriela") # inser as penultimate
guest_list.append("Hugo")

print(guest_list)