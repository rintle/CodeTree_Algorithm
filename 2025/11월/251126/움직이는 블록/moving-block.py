N = int(input())
blocks = []
for _ in range(N):
    blocks.append(int(input()))

height = sum(blocks)//N

ans = 0
for b in blocks:
    ans += abs(height-b)
print(ans//2)