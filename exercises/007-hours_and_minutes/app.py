#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  
  hours = 0
  if secs > 3600:
    hours=int(secs/3600)
    minutes=round(((secs/3600)%1)*60)

  elif secs >=60:
    minutes=int(secs/60)

  return hours,minutes

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))