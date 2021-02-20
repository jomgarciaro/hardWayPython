types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarius = False
joke_evaluation = "Isn't that joke so funny?! {}" #It is just a simple string without format but with a "space" for that

print(joke_evaluation.format(hilarius)) #Here we put format to aprevious string a put the value of the hilarius variable into a {} space.

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
