def solution(X, Y):
    ans = []
    yarr = list(Y)
    for i in range(9,-1,-1) :
        ans += (str(i) * min(X.count(str(i)), Y.count(str(i))))
            
    if len(ans) == 0:
        return "-1"
    elif ans[0] == "0":
        return "0"
    else:
        return "".join(ans)