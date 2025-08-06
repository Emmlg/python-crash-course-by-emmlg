
# Integers

print(2 + 3 )
print(3 - 2 )
print(2 * 3)
print(3 / 2)

## exponentes , usamos ** para exponentes 5^2

print(5**2) 

## python follow order operations

print(3/4*4)
print( 2 + 3*4)

# Floats

print(0.1 + 0.1)
print(0.2+0.2)
print(0.1*2)
print(2 * 0.2)

print( 0.2 + 0.1 ) # be aware to get arbitrary numbers
print(3 * 0.1 )

# Avoiding Type Errors with the str() Function
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)

message = "Happy " + str(age) + "rd Birthday!"
print() # solution

# Integers in Python 2

print("python2.7")
# Instead of 1.5, Python returns 1.
# Division of integers in Python 2 results in an integer with the remainder truncated.
print(3 / 2) 