# def sum(a, b, c):
#     return (a + b + c) / 3
# print(sum(10, 20, 30))

def my_mean(arr):
    my_sum = 0
    for element in arr:
        my_sum += element
    return my_sum/len(arr)

arr = []
ammount_of_numbers = int(input("შეიყვანეთ რამდენი რიცხვის შეყვანა გსურთ: "))

for i in range(ammount_of_numbers):
    x = int(input("შეიყვანეთ რიცხვი " + str(i+1) + " სიისთვის: "))
    arr.append(x)

print(my_mean(arr))