# 12시 방향부터 시계방향으로 제공되기 때문에 비교해야하는 idx는
# 2, 6 을 비교하면 된다.
wheels = [list(map(int,list(input()))) for _ in range(4)]
K = int(input())
wheels = [0] + wheels

def rotate(idx, direction):
    global wheels
    if direction == 1:
        wheels[idx] = [wheels[idx][-1]] + wheels[idx][:-1]
    else:
        wheels[idx] = wheels[idx][1:] + [wheels[idx][0]]

for _ in range(K):
    idx, direction = map(int, input().split())
    isRotate = [False for _ in range(5)]
    rot_dir = [0 for _ in range(5)]
    isRotate[idx] = True
    rot_dir[idx] = direction
    if idx == 1:
        for i in range(2, 5):
            if wheels[i-1][2] == wheels[i][6]:
                break
            else:
                isRotate[i]=True
                direction *= -1
                rot_dir[i] = direction
    if idx == 2:
        if wheels[1][2] != wheels[2][6]:
            isRotate[1] = True
            rot_dir[1] = -direction
        for i in range(3, 5):
            if wheels[i-1][2] == wheels[i][6]:
                break
            else:
                isRotate[i]=True
                direction *= -1
                rot_dir[i] = direction
    if idx == 3:
        if wheels[3][2] != wheels[4][6]:
            isRotate[4] = True
            rot_dir[4] = -direction

        for i in range(2, 0, -1):
            if wheels[i][2] == wheels[i+1][6]:
                break
            else:
                isRotate[i] = True
                direction *= -1
                rot_dir[i] = direction
    if idx == 4:
        for i in range(3, 0, -1):
            if wheels[i][2] == wheels[i+1][6]:
                break
            else:
                isRotate[i]=True
                direction *= -1
                rot_dir[i] = direction
    for i in range(5):
        if isRotate[i]:
            rotate(i, rot_dir[i])
    
print(wheels[1][0]+wheels[2][0]*2+wheels[3][0]*4+wheels[4][0]*8)