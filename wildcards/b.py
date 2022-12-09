import re
def StringChallenge(strParam):

  pattern = ''
  check = strParam.split(' ')[1]
  first = strParam.split(' ')[0]
  index = -1
  for i in first:
      index = index + 1
      if i == '$':
          pattern += '[1-9]'
      elif i == '+':
          pattern += '[a-z]'
      elif i == '*':
          if index != len(first)-1 and first[index+1] == '{' :
              pattern += '[a-z]{'+first[index+2]+'}'
          else:
              pattern += '[a-z]{3}'
  if re.fullmatch(pattern,check):
      return True
  else:
      return False

# keep this function call here 
print(StringChallenge(input()))