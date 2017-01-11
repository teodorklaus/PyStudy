height = int(input('Enter you Height: '))
heightform = (152.4)
weightform = 45
inch = (2.54)
grinch = (0.9)
percent = (0.01)

#Существует формула Наглера, которая позволяет вычислять идеальное соотношение веса и роста.
# На 152,4 см роста должно приходиться 45 кг веса. На каждый дюйм (то есть 2,54 см) сверх 152,4 см
# должно быть еще по 900 г. Плюс еще 10% от полученного веса.
if height < 152.4:
    weight = ((weightform - (((heightform - height) / inch) * grinch)) + ((weightform - (((heightform - height) / inch) * grinch))) * percent)
else:
    weight = ((weightform + (((height - heightform) / inch) * grinch)) + ((weightform + (((heightform + height) / inch) * grinch))) * percent)

percentofweight  = weight * percent
print ('You optimal weight is: ' + str(weight) + ' Plus/minus ' + str(percentofweight) + ' Kg')
print ('If you weight is more then this you need lose weight')
print ('If you weight is more then this you need dial weigh')