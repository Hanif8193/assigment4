
def in_range(n, low, high):
    """
    یہ فنکشن چیک کرتا ہے کہ آیا n عدد low اور high کے درمیان ہے (دونوں حدود شامل ہیں)۔
    """
    return low <= n <= high  # اگر n low اور high کے درمیان ہو، تو True واپس کرے گا

# ٹیسٹ کرنے کے لئے، آپ اس فنکشن کو main میں کال کر سکتے ہیں
def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the low range: "))
    high = int(input("Enter the high range: "))
    
    # فنکشن کو کال کریں اور نتیجہ پرنٹ کریں
    if in_range(n, low, high):
        print(f"{n} is in the range between {low} and {high}.")
    else:
        print(f"{n} is not in the range between {low} and {high}.")

# اسکرپٹ کو چلانے کے لئے
if __name__ == '__main__':
    main()
