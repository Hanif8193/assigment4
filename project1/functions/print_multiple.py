def print_multiple(message, repeats):
   
   
    for _ in range(repeats):
        print(message)

def main():
  


    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # پیغام کو مخصوص تعداد میں پرنٹ کریں
    print_multiple(message, repeats)

# اسکرپٹ کو چلانے کے لئے
if __name__ == '__main__':
    main()