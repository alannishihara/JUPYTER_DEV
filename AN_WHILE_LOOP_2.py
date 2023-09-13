answer = 7

while True:
    guess1 = input("\nEnter a number between 1 and 10: ")
    guess2 = int(guess1)
    diff = guess2 - answer
    if guess2 == answer:
       print(f"\nYou guessed CORRECTLY!\n")
    elif guess2 < answer:
       print(f"\nSorry, you guessed TOO LOW by {abs(diff)}\n")
    elif guess2 > answer:
        print(f"\nSorry, you guessed TOO HIGH by {abs(diff)}\n")
    break