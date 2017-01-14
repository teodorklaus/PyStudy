day = int(input('Please enter day of week: '))
time = float(input('Please enter call duration: '))
discount = (0.02)
uahhour = (0.60)

price = time * uahhour
weekprice = price - (price * discount)

print ('Your price = ' + str(price) if day >= 1 and day <= 5 else ('Your price with 20% discount = ' + str(weekprice)))