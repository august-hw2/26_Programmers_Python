from collections import Counter

def solution(n, control):

    counter = Counter(control)

    return n + counter['w']*1 + counter['s']*(-1) + counter['d']*10 + counter['a']*(-10)