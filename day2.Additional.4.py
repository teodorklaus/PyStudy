speed1 = float(input('Enter speed in KM/H: '))
speed2 = float(input('Enter speed in M/S: '))

print ('Speed KM/H more, then speed M/S.' if float(speed1 * 0.2777777777778) > float(speed2) else 'Speed M/S more, then speed KM/H.')