'''
가장 바깥을 제거하는 방법밖에 없다. 양 끝단
'''
N = int(input())
line = []
for _ in range(N):
    a, b = map(int, input().split())
    line.append((a,b))
line.sort()
line2 = sorted(line, key=lambda x: x[1])
# 가장 바깥의 선분이 같은 선분이라면 (가장 긴 선분임)
if line[0] == line2[-1]:
    print(line2[-2][1] - line[1][0])
else:
    print(min(line2[-1][1] - line[1][0], line2[-2][1] - line[0][0]))
