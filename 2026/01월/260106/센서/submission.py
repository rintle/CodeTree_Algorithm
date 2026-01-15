N = int(input())
K = int(input())
sensors = sorted(list(map(int, input().split())))
diff = []
prev = sensors[0]
for i in range(1, N):
    diff.append(abs(prev - sensors[i]))
    prev = sensors[i]
print(sum(sorted(diff,reverse=True)[K-1:]))
'''
문제를 잘 이해 못했음.
각 센서끼리 거리를 구한 뒤,
가장 거리가 먼 센서들의 위치를 K-1개 만큼 지워내면
총 K개의 구간으로 센서들을 나눌 수 있다.

거리가 가장 먼 곳들을 끊어낸다.

3 / 6 7 8 10 / 12 14 15 / 18 / 20
'''