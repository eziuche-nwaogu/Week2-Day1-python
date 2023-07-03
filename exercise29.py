# The code below represents a conditional statement using the if statement. This expression evaluates to True or False after which the code executes or does something else
# The code under the if statement is indented four spaces as this is to show that it is part of the if statement or a function. It is also the standard
# If the code under the if ststement is not indented the code will throw up an error. The initial values for the people, cats and dogs could also be changed and the code will run based on the new values
people = 20
cats = 30
dogs = 15
if people < cats:
    print("Too many cats! The world is doomed!")
if people > cats:
    print("Not many cats! The world is saved!")
if people < dogs:
    print("The world is drooled on!")
if people > dogs:
    print("The world is dry!")
dogs += 5
if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("People are dogs.")
