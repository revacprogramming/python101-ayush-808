#3.1
hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter the Rate:"))
if h <= 40:
 	print( h  * rate)
elif h > 40:
	print(40* rate + (h-40)*1.5*rate)




#3.3
score = float(input("Enter the score: "))
if (score<=1.0 and score >= 0.0):
    if (score>=0.9):
      print("A")
    elif(score<0.9 and score>=0.8):
      print("B")
    elif(score<0.8 and score>=0.7):
      print("C")
    elif(score<0.7 and score>=0.6):
      print("D")
    elif(score<0.6):
      print("F")
    else:
      print("THe score entered is wrong")