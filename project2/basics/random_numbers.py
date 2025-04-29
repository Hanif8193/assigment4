import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Generate N_NUMBERS random numbers in the range [MIN_VALUE, MAX_VALUE]
    for _ in range(N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value, end=" ")

if __name__ == '__main__':
    main()
