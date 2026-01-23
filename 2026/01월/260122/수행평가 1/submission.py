'''
2026.01월.260122.수행평가 1.submission의 Docstring
아니 문제 너무 어려운데
'''
# 완전한 코드
N, M = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7

for length in range(1, N + 2):
    seen = set()
    for i in range(max(0, N - length + 1)):
        subseq = tuple(A[i:i+length])
        seen.add(subseq)
    
    found = len(seen)
    total = pow(M, length, MOD)
    
    if found < M ** length or length > N:
        print(length, (total - found + MOD) % MOD)
        break