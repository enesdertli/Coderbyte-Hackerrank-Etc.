def BracketMatcher(strParam):
    result = 0 
    for char in strParam:
        if char == "(":
            brackets +=1
        elif char == ")":
            brackets -= 1
        if brackets < 0:
            break
    if brackets == 0:
        result = 1
    return result
print(BracketMatcher(input()))