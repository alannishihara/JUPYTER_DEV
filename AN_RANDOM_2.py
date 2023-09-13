import random

n1 = input("\nEnter lower end of numeric range (an integer between 1 and 5): ")
n2 = input("Enter upper end of numeric range (an integer between 6 and 10): ")

random_number = random.randint(int(n1), int(n2))  # Generates a random integer between n1 and n2 (inclusive)

while True:
    if 1 <= random_number <=5:
        print(f"\nThe random number generated is: {random_number}\n")
        print(f"...which is BETWEEN 1 AND 5\n")
        break
    else:
        print(f"\nThe random number generated is: {random_number}\n")
        print(f"...which is BETWEEN 6 AND 10\n")
        break