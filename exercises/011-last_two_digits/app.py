#Complete the function to print the last two digits of an interger greater than 9. 
def last_two_digits(num):
    numstr=str(num)

    return int(numstr[len(numstr) - 2] + numstr[len(numstr)-1])

#Invoke the function with any interger greater than 9.
print(last_two_digits(1234))
