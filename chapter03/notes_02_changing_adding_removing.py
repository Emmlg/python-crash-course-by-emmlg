
# Changing, Adding, and Removing Elements

## changing data
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
## Adding Elements to a List (Appending Elements to the End of a Lis)
print("------ADDING ELEMENTS-----------")

motorcycles.append('ducati') # add at the end of a list
print(motorcycles)

### dynamic list
print("-------dynamic List----------")

motorcycles = [] 
motorcycles.append('honda') 
motorcycles.append('yamaha') 
motorcycles.append('suzuki') 
print(motorcycles)

### Inserting Elements into a List

print("----- Inserting Elements into a List -------")
motorcycles = ['honda', 'yamaha', 'suzuki'] 
motorcycles.insert(0, 'ducati')

motorcycles.insert(-1, 'ducati_last') #Python convierte el -1 así:
                                      #if index < 0:
                                      #   index += len(lista)

print(motorcycles)

## Removing Elements from a List
print("------- Removing Elements from a List---------")


motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
del motorcycles[0] # remove NO Allow to ACESS VALUE
print(motorcycles)

print("- Removing an Item Using the pop() Method - ")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() # it's a value we can ACESS and REMOVE 
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
last_owned = motorcycles.pop() 
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# Popping Items from any Position in a List
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

