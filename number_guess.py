import random

last_num = int(
    input("Enter LAST number till you want to guess like(1 - 10) - "))
num = random.randint(1, last_num)

while True:
    guess = int(input("Guess number between 1 to number - "))
    if guess == num:
        print('"Well guessed!"')
        break
    else:
        continue
