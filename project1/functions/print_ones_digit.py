def print_ones_digit(num):
    """
    یہ فنکشن ایک عدد کے آخری ہندسے (ones digit) کو پرنٹ کرتا ہے۔
    """
    ones_digit = num % 10  # % 10 سے ہمیں آخری ہندسہ ملتا ہے
    print(f"The ones digit is {ones_digit}")

def main():
    # صارف سے عدد حاصل کریں
    num = int(input("Enter a number: "))
    
    # آخری ہندسہ پرنٹ کریں
    print_ones_digit(num)

# اسکرپٹ کو چلانے کے لئے
if __name__ == '__main__':
    main()

