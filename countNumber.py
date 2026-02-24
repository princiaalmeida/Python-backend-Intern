numbers = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter the number to count: "))

count = 0
for num in numbers:
    if num == target:
        count += 1

# Display result
print(f"The number {target} appears {count} times in the list.")
