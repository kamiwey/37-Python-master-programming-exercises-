#Complete the function to return the tens digit of a given interger
def tens_digit(num):

  numstr=str(num)

  return int(numstr[len(numstr)-2])




#Invoke the function with any interger.
print(tens_digit(1234))