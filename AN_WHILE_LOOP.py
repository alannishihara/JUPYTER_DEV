answer = 7

prompt = "\nGuess a number between 0 and 10\n"

while True:
    guess1 = input("\nEnter your guess here: ")
    guess2 = int(guess1)
    diff = guess2 - answer
    if guess2 == answer:
       print(f"\nYou are CORRECT!\n")
    if guess2 < answer:
       print(f"\nSorry, you are too LOW by {abs(diff)}\n")
    elif guess2 > answer:
        print(f"\nSorry, you are too HIGH by {abs(diff)}\n")
    break