#Complete the function to return the respective number of the century
#HINT: You may need to import the math module.
import math

def century(year):

  century=year/100
  if str(year)[0] !=0:
    century=round(year/100)+1
  if str(year)[0] == 0:
    century=round(year/100)

  return century



#Invoke the function with any given year. 
print(century(1801))