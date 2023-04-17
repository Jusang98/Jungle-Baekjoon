import sys


def histo(arr, start, end):
    if start == end:
        return arr[start]
    else:
        mid = (start + end) // 2
        width = 2  # 너비
        left = mid  # 경계 왼쪽
        right = mid + 1  # 경계 오른쪽
        min_height = min(arr[left], arr[right])  # 둘 중에 작은 값
        big_square = min_height * 2  # 경계를 두고 정해지는 직사각형의 크기
        while True:
            if (arr[left] == 0 or left == start) and (arr[right] == 0 or right == end):
                # 왼쪽, 오른쪽 경계값이 0이거나 더이상 이동할수없을떄
                break
            elif arr[left] == 0 or left == start:
                if arr[right + 1] < min_height:
                    min_height = arr[right + 1]
                right += 1
            elif arr[right] == 0 or right == end:
                if arr[left - 1] < min_height:
                    min_height = arr[left - 1]
                left -= 1
            else:  # 왼쪽 오른쪽 모두 이동 가능 할 경우
                if arr[left - 1] > arr[right + 1]:  # 왼쪽 값이 더 크고
                    if arr[left - 1] < min_height:  # min_height 보다 값이 작으면
                        min_height = arr[left - 1]  # min_height를 갱신해준다
                    left -= 1  # 다시 이동
                else:  # 오른쪽 값이 더 크고
                    if arr[right + 1] < min_height:  # min_height보다 값이 작으면
                        min_height = arr[right + 1]  # 갱신
                    right += 1
            width += 1

            big_square = max(big_square, min_height * width)  # 기존의 tmp와
        return max(histo(arr, start, mid), histo(arr, mid + 1, end), big_square)


while True:
    square = list(map(int, sys.stdin.readline().split()))
    if square[0] == 0:
        break
    print(histo(square, 1, len(square) - 1))
