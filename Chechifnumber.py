nums = list(map(int, input("Enter numbers separated by space: ").split()))
for num in nums:
    if 50 <= num <= 100:
        print(num, "lies between 50 and 100.")
    else:
        print(num, "does NOT lie between 50 and 100.")
