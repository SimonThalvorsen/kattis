import sys
lowest = 1
highest = 1000
guess = 500
for i in range(10):
    print(guess)
    sys.stdout.flush()
    inp = input()
    if inp=="higher":
        lowest = guess + 1
        guess = (lowest+highest)//2
    elif inp=="lower":
        highest = guess - 1
        guess = (lowest + highest)//2
    else:
        exit()
