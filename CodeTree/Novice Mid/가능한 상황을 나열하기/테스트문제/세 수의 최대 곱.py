# 양수 top 3를 추출한다
# 음수 인버스 top 2를 추출한다
# 거기에서 골라서 곱해본다. 인버스top2 x top1 vs top3곱
# 아니다. 모든 경우를 조사해야 한다.

# 양수를 3개 고르는 경우
# 가장 큰 양수 3개를 선택한다.

# 양수 1개, 음수 2개 고르는 경우
# 절대값이 큰 수들만 고른다.

# 음수를 3개 고르는 경우
# 가장 작은 음수 3개를 선택한다.

# 양수 2개, 음수 1개 고르는 경우 (N이 3밖에 없다면 이 경우에 해당한다.)
# 절대값이 작은 수들만 고른다

# N개의 정수에 0이 포함되어 있는 경우 - 0을 포함한 값을 고르는 경우
# 0을 포함해준다.

N = int(input())

nums = list(map(int, input().split()))

pos, neg = [], []

for n in nums:
    if n >= 0:
        pos.append(n)
    else:
        neg.append(n)

pos.sort(reverse=True)
neg.sort()

ans = -1000000001
# 양수 3개인 경우
if len(pos) >= 3:
    val = pos[0]*pos[1]*pos[2]
    ans = max(ans, val)

# 양수 1개, 음수 2개인 경우
if len(pos)>=1 and len(neg) >= 2:
    val = pos[0]*neg[0]*neg[1]
    ans = max(ans, val)

# 양수 2개, 음수 1개인 경우
if pos[-1] and len(pos)>=2 and len(neg)>=1:
    val = pos[-2]*pos[-1]*neg[-1]
    ans = max(ans, val)

# 음수 3개인 경우
if len(neg) >= 3:
    val = pos[-3]*pos[-2]*pos[-1]
    ans = max(ans, val)
# 0이 포함된 경우
if pos[-1] == 0:
    ans = max(ans, 0)

print(ans)