def solution(num_list):
    str1 = ''.join(str(i) for i in num_list if i % 2)
    str2 = ''.join(str(i) for i in num_list if i % 2 == 0)

    return int(str1)+int(str2)