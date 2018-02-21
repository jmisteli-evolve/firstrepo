fruit_basket = ["Tomato", "BlueBerry", "Apple", "Orange", "Pineapple"]

guess = raw_input("Guess a fruit \n")
if guess.isalpha():
	if guess in fruit_basket:
		print("You picked a fruit")
	else:
		print("You dind't pick a fruit")
else:
	print("Next time pick a string")
