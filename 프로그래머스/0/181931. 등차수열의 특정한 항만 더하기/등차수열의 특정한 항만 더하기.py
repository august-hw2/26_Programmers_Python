def solution(a, d, included):
    return sum(a+(n)*d for n in range(len(included)) if included[n])