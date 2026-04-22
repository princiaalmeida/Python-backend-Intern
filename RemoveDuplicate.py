user_input = input("Enter numbers separated by space: ")
my_list = list(map(int, user_input.split()))
unique_list = list(dict.fromkeys(my_list))
print("List after removing duplicates:", unique_list)
