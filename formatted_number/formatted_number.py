import re
def StringChallenge(strArr):
  test_string = strArr[0]

  pattern = '\d+\.\d+$'
  pattern2 = '\d{1,3},(\d{3},)*(\d{3}\.)+(\d+$)'
  pattern3 = '^\d+$'
  pattern4 = '\d+,\d+$'

  result = re.match(pattern, test_string)
  result2 = re.match(pattern2, test_string)
  result3 = re.match(pattern3, test_string)
  result4 = re.match(pattern4, test_string)

  if result or result2 or result3 or result4:
    return True
  else:
    return False

# keep this function call here 
print(StringChallenge(input()))