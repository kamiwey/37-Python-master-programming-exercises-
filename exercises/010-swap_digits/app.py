#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  # Your code here
  digit1 = num //10
  digit2 = int(((num/10)%1)*10)

  return int(str(digit2) + str(digit1))
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))
