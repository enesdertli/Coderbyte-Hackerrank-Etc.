import math
def MathChallenge(num):

  if num == 1:
    return 0

  length = num
  zero = length-1
  zeros = ('0'*zero)
  one = '1'
  minimum = one+zeros
  
  int_check = int(math.sqrt(int(minimum)))
  float_check = math.sqrt(int(minimum))

  if int_check < float_check:
    int_check +=1
  return int_check

# keep this function call here 
print(MathChallenge(input()))