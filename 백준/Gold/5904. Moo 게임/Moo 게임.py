import sys


# n 에서 전차수를 뺄때 1이면 n return은 m이다 나머진 전부 o

def moo(n, k, l):  # n번째 글자,k는 차수, #l은 전 차수의 길이
    S0 = ['m', 'o', 'o']
    lk = 2 * l + k + 3  # lk = l + (k+3) + l 새로운 차수의 길이
    if n <= 3:
        print(S0[n - 1])
        return
    if lk < n:  # lk가 n보다 작을 경우
        moo(n, k + 1, lk)
    else:
        if l < n <= l + k + 3:  # n이 전차수길이 보다 크고 다음 차수로 가는 길이보다 작을떄
            if n - l == 1:  # n-l = 1일때만 'm'이 있고 나머지는 'o'로 채워진다.
                print('m')
            else:
                print('o')
            return
        else:  # 범위안에 없을떄 재귀
            moo(n - (l + k + 3), 1, 3)


N = int(sys.stdin.readline())
moo(N, 1, 3)
