# 두 사람 사이가 가장 좁은 경우 사이로 다른 사람을 넣어야 한다.
# 최대 이동 개수기 때문에, 더 좁은 범위에서 넓은 범위로 이동해야 한다.
a, b, c = map(int, input().split())
ans = 0
while a+1 != b or b+1 != c:
    dist1, dist2 = b-a, c-b
    if dist1 <= dist2:
        a, b, c = b, b+1, c
    elif dist1 > dist2:
        a, b, c = a, a+1,b
    ans += 1
print(ans)