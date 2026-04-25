import random

while True:
	level = input('Choose your difficulty level. 1 for Easy, 2 for Medium, 3 for Hard ?')
	if level == "exit":
		print("Game Exit")
		break
	try:	
		if int(level) == 1 :
			number = random.randint(1,50)
			max_attempts = 10
			print(f'You have {max_attempts} chances')
			
		elif int(level) == 2 :
			number = random.randint(1,100)
			max_attempts = 8
			print(f'You have {max_attempts} chances')
		
		elif int(level) == 3 :
			number = random.randint(1,200)
			max_attempts = 6
			print(f'You have {max_attempts} chances')
				
	except ValueError:
		print("Wrong value entered, please choose only numbers")
		continue
	
	attempt = 0
	
	while attempt < max_attempts :
	
		guess = input("Guess the number :")
		
		if guess == "exit" :
			print("Game Exit")
			break
	
		try:
			guess = int(guess)
		except ValueError :
			print('Please enter numerical value only')
			continue
	
		attempt +=1
		remaining = max_attempts - attempt
	
		if int(guess) > number :
			print('Too High')
			print(f'Total {remaining} chances remain')
			continue
	
		elif int(guess) < number :
			print('Too Low')
			print(f'Total {remaining} chances remain')
			continue
		
		else :
			print(f'You are Winner. Correct number is : {number}, You Win in only {attempt} attempts')
			break
	else :
		print(f"You're Lose !!! Better Luck next time, The number was {number}")

	print("\n--- New Game Starting ---\n")


