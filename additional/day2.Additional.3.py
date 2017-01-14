num = int(input('Enter 3 numeral: '))

list1 = list (str(num))
if list1[0] == list1[1] and list1[1] == list1[2]:
    print ('Entered number has 3 the same numeral: ' + list1[1])
elif list1[0] == list1[1] or list1[1] == list1[2] or list1[0] == list1[2]:
    print ('Entered number has 2 the same numeral!')
elif list1[0] != list1[1] and list1[1] != list1[2] and list1[0] != list1[2]:
    print ('Entered number didnot have the same numeral: ' + str(list1))