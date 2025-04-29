my_list = ["water Melon", "apple", "banana", "grape", "orange"]

def access_element(my_list, index):
    """Return the element at specified index, or an error message if out of range."""
    if 0 <= index < len(my_list):
        return f'Element at index {index}: {my_list[index]}'
    return "Index out of range"

def modified_element(my_list, index, new_value):
    """Modify the element at the specified index."""
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f"Modified element at index {index}: {old_value} -> {new_value}"
    return "Index out of range"

def slice_elements(my_list, start, end):
    """Return a slice of the list from start to end."""
    if 0 <= start <= end <= len(my_list):
        return f'Sliced list: {my_list[start:end]}'
    return "Invalid slice indices"

def list_game():
    print("Welcome to the List Game!")
    my_list = ["water Melon", "apple", "banana", "grape", "orange"]

    while True:
        print("\nCurrent list:", my_list)
        print("Select an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice elements")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter the index of the element to access: "))
            result = access_element(my_list, index)
            print(result)

        elif choice == '2':
            index = int(input("Enter the index of the element to modify: "))
            new_value = input("Enter the new value: ")
            result = modified_element(my_list, index, new_value)
            print(result)

        elif choice == '3':
            start = int(input("Enter the start index for slicing: "))
            end = int(input("Enter the end index for slicing: "))
            result = slice_elements(my_list, start, end)
            print(result)

        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the list game
list_game()

