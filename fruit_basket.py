
def main():
	fruit_basket = ["Tomato", "BlueBerry", "Apple", "Orange", "Pineapple"]
	isWrong = False
	while isWrong == False:
		isWrong = guess_fruit(fruit_basket)

def guess_fruit(basket):
	guess = raw_input("Guess a fruit \n")
	if guess.isalpha():
		if guess in basket:
			print("You picked a fruit")
			return True
		else:
			print("You dind't pick a fruit")
			return False
	else:
		print("Next time pick a string")
main()
