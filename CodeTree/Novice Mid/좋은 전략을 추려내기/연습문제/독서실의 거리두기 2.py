# 새로 온 사람이 왼쪽 끝에 앉을 때
# 새로 온 사람이 오른쪽 끝에 앉을 때
# 양 끝이 아닌 다른 곳에 앉을 때

N = int(input())
seats = list(map(int, list(input())))

ans = 0

largest = 0
leftL, rightL = 0,0
# 가장 먼 거리 찾기
for i in range(N):
    if seats[i]:
        for j in range(i+1, N):
            if seats[j]:
                dist = j-i
                if dist > largest:
                    largest = dist
                    leftL, rightL = i, j
                break
shortest = 1000
leftS, rightS = 0,0
# 가장 짧은 거리 찾기
for i in range(N):
    if seats[i]:
        for j in range(i+1, N):
            if seats[j]:
                dist = j-i
                if dist < shortest:
                    shortest = dist
                    leftS, rightS = i, j
                break
leftdist = 0
# 왼쪽 끝이 0인 경우
if seats[0] == 0:
    seats[0] = 1
    shortest = 1000

    # 가장 짧은 거리 찾기
    for i in range(N):
        if seats[i]:
            for j in range(i+1, N):
                if seats[j]:
                    dist = j-i
                    if dist < shortest:
                        shortest = dist
                    break

    ans = max(ans, shortest)
    seats[0] = 0

# 오른쪽 끝이 0인 경우
if seats[-1] == 0:
    seats[-1] = 1
    shortest = 1000

    # 가장 짧은 거리 찾기
    for i in range(N):
        if seats[i]:
            for j in range(i+1, N):
                if seats[j]:
                    dist = j-i
                    if dist < shortest:
                        shortest = dist
                    break

    ans = max(ans, shortest)
    seats[-1] = 0
    
shortest = 1000

seats[leftL+largest//2] = 1
# 가장 짧은 거리 찾기
for i in range(N):
    if seats[i]:
        for j in range(i+1, N):
            if seats[j]:
                dist = j-i
                if dist < shortest:
                    shortest = dist
                break

ans = max(ans, shortest)

print(ans)