
def add_four_copies(my_list, data):
    for i in range(4):
        my_list.append(data)

def main():
    message = input("Enter a message: ")  # User input for the message
    my_list = []
    print("List before: ", my_list)  # Output: []

    add_four_copies(my_list, message)
    print("List after: ", my_list)

# یہ فنکشن صرف تب چلایا جائے گا جب اس فائل کو براہِ راست run کیا جائے
if __name__ == '__main__':
    main()

