"""list comprehensions"""
"""Also see https://docs.python.org/3/tutorial/datastructures.html"""
squares = []

# for x in range(10):
#     squares.append(x**2)

#Comprehesions
squares = [x**2 for x in range(10)]
print(squares)

#Take only evens
squares = [x**2 for x in range(10) if x%2==0]
print(squares)

#Create a list of 2-tuples like (number, square)
squares = [(x,x**2) for x in range(10) if x%2==0]
print(squares)

