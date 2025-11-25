N = int(input())
score_a, score_b = 0, 0
top = 'Both'

ans = 0
for _ in range(N):
    c,s = input().split()
    s = int(s)
    if c == 'A':
        score_a += s
    else:
        score_b += s
    if score_a > score_b:
        if top != 'A':
            ans += 1
            top = 'A'
    elif score_a < score_b:
        if top != 'B':
            ans += 1
            top = 'B'
    else:
        if top != 'Both':
            ans += 1
            top = 'Both'
print(ans)