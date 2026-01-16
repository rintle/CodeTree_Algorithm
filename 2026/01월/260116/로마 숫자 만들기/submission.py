'''
2026.01월.260116.로마 숫자 만들기.submission의 Docstring
숫자를 위해 
I, V, X, L 사용함.
1, 5,10,50
XXXV = 35
IXI = 12
'''
N = int(input())
data = [1,5,10,50]
used = [False for _ in range(4)]
numbers = [False for _ in range(50*20+1)]
ans = 0
def permutation(num, cnt, start):
    global ans
    if cnt == N:
        if numbers[num]:
            return
        numbers[num]=True
        ans += 1
        return
    for i in range(start, 4):
        permutation(num + data[i], cnt+1, i)
permutation(0, 0, 0)
print(ans)