import re
def StringChallenge(strParam):

  capitalizedArray = []
  badCharacters = [';', ':', '!', "*", "-",'%','^','#','>','<']
  for i in badCharacters:
    strParam = strParam.replace(i, ' ')
  strParam = strParam.split()
  first = strParam[0]
  capitalizedArray.append(first)
  
  for i in strParam[1:]:
    i = i.lower()
    i = i.capitalize()
    
    capitalizedArray.append(i)
  
  string = ''.join(capitalizedArray)
  return string
# keep this function call here 
print(StringChallenge(input()))