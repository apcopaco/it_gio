def comparison(num1, num2):
    if num1 > num2:
        print("The largest number: " + str(num1))
        return num1

    else:
        print("The largest number: " + str(num2))
        return num2
    
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

max1 = comparison(num1, num2)

num1 = int(input("enter the first number again: "))
num2 = int(input("enter the second number again: "))

max2 = comparison(num1, num2)

print(max1 + max2)

