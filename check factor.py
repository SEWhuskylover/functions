def check(bigger, smaller):
    return bigger % smaller == 0


big = int(input("enter a number \n"))
small = int(input("enter the number to check \n"))
if check(big, small):
    print(f"{small} is a factor of {big}")
else:
    print(f"{small} is not a factor of {big}")
