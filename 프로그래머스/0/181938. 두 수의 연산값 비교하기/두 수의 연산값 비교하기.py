def solution(a, b):
    
    ab = int(str(a)+str(b))
    ab2 = 2*int(str(a))*int(str(b))
    
    return max(ab, ab2)