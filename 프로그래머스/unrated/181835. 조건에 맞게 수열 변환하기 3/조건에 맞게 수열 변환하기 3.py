def solution(arr, k):
    answer = []
    for i in arr:
        if(k%2 != 0):
            answer.append( i * k)
        if(k%2 == 0):
            answer.append(i + k)
    return answer