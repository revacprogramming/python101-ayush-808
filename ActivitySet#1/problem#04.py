hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter the Rate:"))
if h <= 40:
 	print( h  * rate)
elif h > 40:
	print(40* rate + (h-40)*1.5*rate)