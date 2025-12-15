from collections import deque
T = int(input())
wheels = []
for _ in range(T):
    wheels.append(deque(map(int,list(input()))))
'''
톱니바퀴가 idx번째에서 시작하는 경우,
해당 톱니바퀴와, 그 이전 혹은 이후 톱니바퀴들을 순회하며
그 옆의 톱니바퀴가 돌아가는지, 아닌지 판단해야한다.

wheels에서 index 2와 6을 비교해야함.
'''
rotation_direction = [0 for _ in range(T)]
def rotate(idx, direction):
    global rotation_direction
    rotation_direction = [0 for _ in range(T)]
    rotation_direction[idx] = direction
    left_idx, left_directions = idx, -direction
    while left_idx > 0:
        next_idx = left_idx - 1
        if wheels[next_idx][2] != wheels[left_idx][6]:
            rotation_direction[next_idx] = left_directions
            left_directions *= -1
            left_idx -= 1
        else:
            break
    right_idx, right_directions = idx, -direction
    while right_idx + 1 < T:
        next_idx = right_idx + 1
        if wheels[next_idx][6] != wheels[right_idx][2]:
            rotation_direction[next_idx] = right_directions
            right_directions *= -1
            right_idx += 1
        else:
            break

def update():
    for idx, direction in enumerate(rotation_direction):
        if direction == 1:
            wheels[idx].appendleft(wheels[idx].pop())
        elif direction == -1:
            wheels[idx].append(wheels[idx].popleft())

def print_log():
    for c in wheels:
        print(*c)

K = int(input())

for _ in range(K):
    cog, direction = map(int, input().split())
    cog -= 1
    rotate(cog, direction)
    # print(rotation_direction)
    update()
ans = 0
for cog in wheels:
    ans += cog[0]
print(ans)