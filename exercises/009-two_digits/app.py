#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):

  digit1 = digit // 10
  digit2 = int(((digit/10)%1)*10)

  return digit1, digit2
   


#Invoke the function with any interger as its argument.
print(two_digits(79))
