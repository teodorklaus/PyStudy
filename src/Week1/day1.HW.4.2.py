max1 = 0
max2 = 0
max3 = 0
min1 = 0
min2 = 0
min3 = 0
maxp = 0
minp = 0


num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3:
    max1 = num1
elif num1 < num2 and num1 < num3:
    min1 = num1

if num2 > num1 and num2 > num3:
    max2 = num2
elif num2 < num1 and num2 < num3:
    min2 = num2

if num3 > num1 and num3 > num2:
    max3 = num3
elif num3 < num1 and num3 < num2:
    min3 = num3

if max1 > max2 and max1 > max3:
    maxp = max1
elif max2 > max3 and max2 > max1:
    maxp = max2
elif max3 > max1 and max3 > max2:
    maxp = max3


if min1 < min2 and min1 < min3:
    minp = min1
elif min2 < min1 and min2 < min3:
    minp = min2
elif min3 < min1 and min3 < min2:
    minp = min3

print ("max: " + str(maxp))
print ("min: " + str(minp))