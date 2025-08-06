
# basics of a list
#Python returns its representation of the list, including the square brackets
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

## how to access to individual item?

print(bicycles[0])
print(bicycles[0].title()) # we can manipulate data
print(bicycles[-1]) # access to the last item


## Using Individual Values from a List

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)


