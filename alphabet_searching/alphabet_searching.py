def StringChallenge(strParam):
  alphabet = []
  for i in range(97,123):
    alphabet.append(chr(i))
  in_alphabet = True
  for i in alphabet:
    if i not in strParam:
      in_alphabet = False
      break
  return in_alphabet
# keep this function call here 
print(StringChallenge(input()))