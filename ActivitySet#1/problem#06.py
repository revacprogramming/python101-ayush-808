# Loops & Iterators

largest = None
smallest = None

while True:
  try:
      num = (input("Enter a number: ")
      
      if num == "done":
          break

      int_num=int(num)
      if largest==None or int_num>largest:
        largest=int_num
      elif smallest==None or int_num<smallest:
        smallest=int_num

  except:
      print("Invalid input")

print("Maximum is",largest)
print("Minimum is",smallest)      