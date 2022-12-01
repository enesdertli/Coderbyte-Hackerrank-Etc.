import re
def StringChallenge(strParam):

  strParam = strParam.split(' ')
  
  rs = []
  for pattern in strParam:
    r = re.findall(r'[0-9]{3}', pattern)
    rs.append(r)
  for r in rs:
    if len(r) != 0:
      return False
    
  rs = []
  for pattern in strParam:
    r = re.findall(r'[0-9]', pattern)
    r = set(r)
    rs.append(r)
  for r in rs:
    if len(r) != 3:
      return False
  return True
  
# keep this function call here 
print(StringChallenge(input()))