def guess_game():
	import random
	score = 5
	print(f"Your Starting Score: {score}")
	while True:
		ran_num = random.randint(1,5)
		try:
			print("Guess a number Between 1 to 5 or Type 'Q' For Quite.")
			input_num = input("Enter Your Guess: ")
			if input_num == "Q":
				print("------GAME OVER------")
				print(f"Final Score: {score}")
				break
			if input_num == "S5+":
				score += 5 
			guess = int(input_num)
			if guess > ran_num:
				print("You Guessed Too high!")
				score -= 1
				print(f"Score: {score}\n")
			elif guess < ran_num:
				print("You Guessed Too Low!")
				score -= 1
				print(f"Score: {score}\n")
			elif guess == ran_num:
				print("Congratulations!, You Win")
				score += 1
				print(f"Score: {score}\n")
			if score <1:
				print(f"Final Score: {score}")
				break
			if score > 10:
				print("Congratulations! YOU MAKE 10+ SCORE.")
				print("------GAME OVER------")
				print(f"Final Score: {score}")
				break
			
		except ValueError:
			print("Please, Enter Valid Number!")

name = input("Enter Your Name: ").strip().capitalize()
print(f"Hello {name}, Welcome To Guess Game! (V3.0)\n") 
ask = input("What Do You Think Would You Win of Lose? (Type Y For Yes Or N For No) : ")
yes = "Y"
no = "N"

if ask == yes:
	print(f"Oh! {name}, You Look Confident! Let's See What Happens!\n")

elif ask == no:
	print("No Confluence, No Problem Let's Go!\n")

else:
	print(guess_game())

guess_game()

