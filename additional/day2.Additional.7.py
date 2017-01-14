num = int(input('Enter numeral range of from 1 to 12: '))

if num >= 1 and num <= 2 or num == 12:
    print ('Winter month: ' + str(num))
elif num >= 3 and num <= 5:
    print ('Spring month: ' + str(num))
elif num >= 6 and num <= 8:
    print ('Summer month: ' + str(num))
elif num >= 9 and num <= 11:
    print ('Autumn month: ' + str(num))
else:
    print ('Error! This numeral not in range of 1 - 12!')