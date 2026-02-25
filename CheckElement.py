user_input = input("Enter tuple elements separated by space: ")
my_tuple = tuple(map(int, user_input.split()))
element = int(input("Enter element to search: "))
if element in my_tuple:
    print("Element exists in the tuple")
else:
    print("Element does not exist in the tuple")
