'''
2026.01월.260116.카드 놓기.submission의 Docstring
n장을 바닥에 나란히. 1이상 99이하.
k장을 선택, 가로로 나란히 정수.
가능한 총 정수 가지수?
'''
n = int(input())
k = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

pick = []
used = [False for _ in range(n)]
found = set()
def choose(cnt):
    if cnt == k:
        num = int(''.join(pick))
        found.add(num)
        return
    for i in range(n):
        if used[i]:
            continue
        pick.append(str(data[i]))
        used[i] = True
        choose(cnt+1)
        pick.pop()
        used[i] = False
choose(0)
print(len(found))
