nums = [15 , 10 , 12 , 98 , 770]

guess = 0

while guess != 'q':
    guess = input("Guess the number(enter 'q' to quit):")
    if guess == 'q':
        break
    elif int(guess) in nums:
         print("You got it right")
    else:
        print("You did not guess it right")

