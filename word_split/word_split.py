def ArrayChallenge(strArr):

  aimString = strArr[0]
  cases = [strArr[1]]
  cases = cases[0]
  cases = cases.split(',')


  mayStart = []
  
  for i in cases:
    length = len(i)
    
    if i == aimString[0:(length)]:
      
      mayStart.append(i)
  if len(mayStart) != 0:
    for i in mayStart:
      length = len(i)
      a = aimString[length:]
      first = i
      last = a
      
      if a in cases:
        
        return first + ',' + last
        
        


# keep this function call here 
print(ArrayChallenge(input()))