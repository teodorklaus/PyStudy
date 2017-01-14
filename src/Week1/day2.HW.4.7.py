num1 = int(input())
num2 = int(input())


if num1 % num2 == 0:
    print ('True: ' + str(num1 / num2))
elif num2 % num1 == 0:
    print ('True: ' + str(num2 / num1))
elif num1 / num2:
    print ('False: ' + str(num1 / num2))
elif num2 / num1:
    print ('False: ' + str(num2 / num1))