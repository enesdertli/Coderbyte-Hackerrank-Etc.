def ArrayChallenge(strArr):
 
 firstString = strArr[0]
 secondString = strArr[1]
 newString = ''
 for i in range(len(firstString)):
   if firstString[i] == secondString[i] == '1':
     newString = newString + '1'
   else:
     newString = newString + '0'
  
 return newString
 
 
# keep this function call here
print(ArrayChallenge(input()))