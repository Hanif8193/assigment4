INCHES_IN_FOOT: int = 12 

def main():
    feet: float = float(input("Enter feet: "))
    
    # Convert feet to inches
    inches: float = feet * INCHES_IN_FOOT
    
    print(f"{feet} feet is equal to {inches} inches")

if __name__ == '__main__':
    main()