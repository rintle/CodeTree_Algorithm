def getRank(s1, s2, s3):
    if s1 == s2 == s3:
        return 1
    # s1가 가장 큰 경우
    elif s1 > s2 and s1 > s3:
        return 2
    # s2가 가장 큰 경우
    elif s2 > s1 and s2 > s3:
        return 3
    # s3가 가장 큰 경우
    elif s3 > s1 and s3 > s2:
        return 4
    # s1, s2가 같고 가장 큰 경우
    elif s1 == s2 and s1 > s3:
        return 5
    # s1, s3가 같고 가장 큰 경우
    elif s1 == s3 and s1 > s2:
        return 6
    # s2, s3가 같고 가장 큰 경우
    elif s2 == s3 and s2 > s1:
        return 7

N = int(input())
s1, s2, s3 = 0,0,0

ans = 0
for _ in range(N):
    c, s = input().split()
    s = int(s)
    if c == 'A':
        if getRank(s1, s2, s3) != getRank(s1+s, s2, s3):
            ans += 1
        s1 = s1+s
    elif c == 'B':
        if getRank(s1, s2, s3) != getRank(s1, s2+s, s3):
            ans += 1
        s2 = s2+s
    else:
        if getRank(s1, s2, s3) != getRank(s1, s2, s3+s):
            ans += 1
        s3 = s3+s
print(ans)