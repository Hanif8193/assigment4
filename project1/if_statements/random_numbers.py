
import random

N_NUMBERS : int = 5
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    for i in range(N_NUMBERS):
        # Generate a random number between MIN_VALUE and MAX_VALUE (inclusive)
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        print(random_number)
    
    pass

if __name__ == '__main__':
    main()