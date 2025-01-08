def main():
    lowest = 1
    highest = 1000
    guess = 500
    for _ in range(10):
        print(guess)
        inp = input()
        if inp=="higher":
            lowest = guess + 1
            guess = (lowest+highest)//2
        elif inp=="lower":
            highest = guess - 1
            guess = (lowest + highest)//2
        else:
            exit()

if __name__ == "__main__":
    main()
