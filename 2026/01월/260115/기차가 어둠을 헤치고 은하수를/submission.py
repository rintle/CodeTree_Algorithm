'''
2026.01월.260115.기차가 어둠을 헤치고 은하수를.submission의 Docstring
N개의 기차
20개의 일렬로 된 좌석이 있음. 한개의 좌석에는 한명의 사람이 탈 수 있음.
M개의 명령이 주어짐.

1 i x : i번째 기차의 x번째 좌석에 사람을 태운다.
2 i x : i번째 기차의 x번째 좌석에 앉은 사람은 하차.
3 i : i번째 기차에 앉아있는 승객들이 모두 한칸씩 뒤로 간다.
      k번째는 k+1번째로 가고, 20번째 자리의 사람은 명령 후 하차한다.
4 i : i번째 기차에 앉아있는 모든 승객이 앞으로 한칸씩 간다.
0b100000000000000000000 : 1<<20
'''
N, M = map(int, input().split())
train = [0 for _ in range(N)]

def printTrain():
    print('-'*20)
    for t in train:
        print(f'{t:021b}')

for _ in range(M):
    command = tuple(map(int, input().split()))
    if command[0] == 1:
        idx, x = command[1:]
        idx -= 1
        x -= 1
        train[idx] |= (1<<x)
    elif command[0] == 2:
        idx, x = command[1:]
        idx -= 1
        x -= 1
        if train[idx] & (1<<x):
            train[idx] -= (1<<x)
    elif command[0] == 3:
        idx = command[1]
        idx -= 1
        train[idx] = train[idx]<<1
        if train[idx] & 1<<20:
            train[idx] -= 1<<20
    else:
        idx = command[1]
        idx -= 1
        train[idx] = train[idx]>>1

checkDup = [False for _ in range(1<<20)]
cnt = 0
start = 0
once = True
for t in train:
    if not checkDup[t]:
        cnt += 1
        checkDup[t] = True
print(cnt)
'''
3 13
1 1 8
1 1 6
1 1 4
1 1 2
1 3 8
1 3 6
1 3 4
1 3 2
1 2 6
1 2 4
1 2 2
1 2 1
3 2

'''