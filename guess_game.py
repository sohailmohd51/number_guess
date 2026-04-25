import random

level = int( input('Choose your difficulty level. 1 for Easy, 2 for Medium, 3 for Hard ?'))

if level == 1 :
	number = random.randint(1,50)
	max_attempts = 10
	print('You have ',max_attempts,' chances')
	
elif level == 2 :
	number = random.randint(1,100)
	max_attempts = 8
	print('You have ',max_attempts,' chances')

else :
	number = random.randint(1,200)
	max_attempts = 6
	print('You have ',max_attempts,' chances')


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
if attempt == max_attempts and guess != number :
	print(f"You're Lose !!! Better Luck next time, The number was {number}")


