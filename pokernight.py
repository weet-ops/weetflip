import random
import time


print("weetflip - A very accurate simulation of the casino")
print("Base code by ImmuneSnow, modified by weet.")
input("Press any key to start wasting your life away.")
time.sleep(1)

def coin_flip():
    return 'H' if random.randint(0, 1) else 'T'

def main():
    chips = 200
    money = 100
    print("You currently have " + str(chips) + " chips.")
    print(" ")
    print("You currently have " + str(money) + " dollars in your wallet.")
    while chips > 0:
        try:
            bet = int(input(f"You have {chips} chips. How many would you like to bet on the coin flip? "))
        except ValueError:
            print("Invalid amount. Please enter an integer.")
            continue
        if bet > chips:
            print("You can't bet more than you have.")
            continue
        guess = input("Enter 'H' for heads or 'T' for tails: ").upper()
        flip = coin_flip()
        if guess == flip:
            print("You won!" + str(bet) + " chips")
            chips += bet
        else:
            print("You lost! -" + str(bet) + " chips")
            chips -= bet
        print(f"You now have {chips} chips.\n")
    print("You ran out of chips.")

if __name__ == "__main__":
    main()
