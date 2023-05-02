import sys

input = sys.stdin.readline
N, K = map(int, input().split())
products = list(map(int, input().split()))
multi_tab = [0] * N
ans = 0
change = maximum = 0

while products:
    product = products[0]
    # 멀티탭에 동일한 제품이 꽂혀있을 경우 -> skip
    if product in multi_tab:
        products.remove(product)    # 멀티탭에 꽂았으니 제품 사용 순서 리스트에서 삭제
        continue

    # 멀티탭에 빈자리가 있을 경우 -> 빈자리에 해당 제품 꽂는다.
    elif 0 in multi_tab:
        multi_tab[multi_tab.index(0)] = product
        products.remove(product)

    # 멀티탭에 빈자리가 없을 경우
    else:
        for mt in multi_tab:
            # 멀티탭에 꽂혀있는 제품 중 이후에 꽂는 제품이 없는 경우
            # 이후에 꽂는 제품이 없는 제품을 빼주고 탐색중인 제품을 꽂는다.
            if mt not in products:
                change = mt
                break

            # 멀티탭에 꽂혀있는 제품 중 가장 나중에 사용하는 제품을 고름.
            # -> 가장 나중에 사용하는 제품을 뽑고 탐색하고 있는 제품을 꽂는다.
            elif products.index(mt) > maximum:
                maximum = products.index(mt)
                change = mt

        multi_tab[multi_tab.index(change)] = product
        products.remove(product)
        maximum = 0
        ans += 1

print(ans)