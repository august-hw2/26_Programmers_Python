def solution(n):
    
    if n%2:
        return pow((n+1)//2,2)
    else:
        return (n*(n+1)*(n+2))//6