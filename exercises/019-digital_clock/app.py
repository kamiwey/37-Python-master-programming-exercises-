#Complete the function to return how many hrs and min are displayed on the 24th digital clock.
def digital_clock(n):
  hours= n/60
  if hours>60:
    hours/60

  return int(hours), int((hours%1)*60)

#Invoke the function with any interger (seconds after midnight)
print(digital_clock(150))
