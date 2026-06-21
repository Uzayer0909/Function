def add(a,b):
    return a+b


def subtract(a,b):
    return a-b


def mul(a,b):
    return a*b


def div(a,b):
    return a/b



print("Please select the operation")

print("a, Addition")

print("b, Subtract")

print("c, Multiplication")

print("d, Divide")


choice = input("Enter your choice (a/b/c/d):")


a = int(input("Enter the first number:"))

b = int(input("Enter the second number:"))

if choice == "a":
    print(f"{a}+{b}={add(a,b)}")


elif choice == "b":
    print(f"{a}-{b}={subtract(a,b)}")

elif choice == "c":
    print(f"{a}x{b}={mul(a,b)}")

elif choice == "d":
    print(f"{a}/{b}={div(a,b)}")

else:
    print("invalid input")


