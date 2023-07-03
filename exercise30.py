# Define a varialbe with an integer value
people = 30
cars = 40
trucks = 15
# Check if cars is greater than people
if cars > people:
    print("We should take the cars.")
# Otherwise check if car is less than people
elif cars < people:
    print("We should not take the cars.")
# If neither condition is true
else:
    print("We can't decide.")
# Check if trucks is greater than cars
if trucks > cars:
    print("That's too many trucks.")
# Otherwise check if trucks is less than cars
elif trucks < cars:
    print("Maybe we could take the trucks.")
# If neither condition is true
else:
    print("We still can't decide.")
# Check if people is greater than trucks
if people > trucks:
    print("Alright, let's just take the trucks.")
# Otherwise print out another stetement
else:
    print("Fine, let's stay home then.")
