
import random

NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")
    return die1  # Return die1 if you want to track it

def main():
    die1 = 10
    print(f"Die 1 in main() starts as: {die1}")

    for _ in range(3):
        die1 = roll_dice()  # You can update die1 if needed
        print(f"Die 1 in main() is now: {die1}")

if __name__ == "__main__":
    main()
