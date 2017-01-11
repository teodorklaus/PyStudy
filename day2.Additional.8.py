sum = float(input('Enter purchase amount: '))

if sum >= 1000:
    discount = (sum * 0.1)
    sum = sum - discount
    print ('You need to pay: ' + str(sum) + 'And your discount is: ' + str(discount))
else:
    print ('You need to pay: ' + str(sum) + 'Your didnot have discount!')