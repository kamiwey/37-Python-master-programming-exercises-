#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  sum=0
  numstr=str(num)
  for i in range(0, len(numstr)):
    sum += int(numstr[i])

  return sum


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))