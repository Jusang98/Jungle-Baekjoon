def solution(s):
    count1 = 0 
    count2 = 0
    answer = 0
    x = ""
    for i in s:
        if count1 == count2:
            count1 +=1
            x = i
            answer +=1
        elif i == x:
            count1 +=1
        else:
            count2 +=1
    return answer