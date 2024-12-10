num = int(input("Enter the number where the countdown should begin"))

while num > 0:
    num = num-1
    if num == 5:
        continue
    print(num)