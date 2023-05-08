def solution(number, limit, power):
    answer = 0
    for weapon in range(1,number+1):
        cnt =0
        for num in range(1,int(weapon**(1/2))+1):
            if weapon % num ==0:
                cnt+=1
                if num <weapon//num:
                    cnt+=1
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer