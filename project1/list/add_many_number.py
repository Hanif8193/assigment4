
from typing import List

def add_one_number(number: int) -> int:
    total_so_far: int = 0
    total_so_far += number
    return total_so_far

def add_many_number(numbers: List[int]) -> int:
    return sum(numbers)

def main():
    
    numbers: List[int] = [1, 2, 3, 4, 5] 
    sum_of_number: int = add_many_number(numbers)  # ایک نمبر کا مجموعہ (بس وہی نمبر واپس آئے گا)
    print(sum_of_number)

if __name__ == '__main__':
    main()
