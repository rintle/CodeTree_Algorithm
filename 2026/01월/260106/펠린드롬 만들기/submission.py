name = list(input())
alpha_cnt = {}
for i in range(26):
    alpha_cnt[chr(ord('A')+i)] = 0
for n in name:
    alpha_cnt[n] += 1

odd_cnt = 0
odd_rpt = 0
odd_ch = ''
ans = ''
for k, v in alpha_cnt.items():
    if v == 0:
        continue
    elif v % 2 == 0:
        ans += k*(v//2)
    elif v % 2 == 1:
        odd_cnt += 1
        ans += k*(v//2)
        odd_ch=k
if odd_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    ans = ans+odd_ch+ans[::-1]
    print(ans)