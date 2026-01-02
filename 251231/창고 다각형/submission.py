'''
251231.창고 다각형.submission의 Docstring
왼쪽면을 기준으로 정렬한 뒤,
나보다 큰게 나올 때 까지 같은 높이로 이동한다.
가장 큰 위치를 기억해둔 뒤, 가장 큰 기둥부터 오른쪽에 있는 기둥 중
가장 큰 기둥까지가 최소 넓이다.
만약 기둥이 가장 오른쪽에 있다면 그것대로가 최소 넓이다.
'''

pillars = []
N = int(input())
for _ in range(N):
    pillars.append(tuple(map(int, input().split())))
pillars.sort(key=lambda x: x[0])
center_pillar = max(pillars, key=lambda x: x[1])
center_pillar_idx = pillars.index(center_pillar)
left_pillars = pillars[:center_pillar_idx+1]
right_pillars = pillars[center_pillar_idx:]
right_pillars.reverse()
# for p in right_pillars:
#     print(p)
ans = 0
# 가장 높은 기둥이 가장 왼쪽에 있는지 여부 체크를 위함
if left_pillars:
    prev_x, prev_y = left_pillars[0]
    for i in range(1, len(left_pillars)):
        x, y = left_pillars[i]
        if y < prev_y:
            continue
        ans += (x-prev_x)*prev_y
        prev_x, prev_y = x, y

if right_pillars:
    prev_x, prev_y=right_pillars[0]
    prev_x += 1
    for i in range(1, len(right_pillars)):
        x, y = right_pillars[i]
        x += 1
        if y < prev_y:
            continue
        ans += (prev_x-x)*prev_y
        prev_x, prev_y = x, y
        
        # if prev_y 
ans += center_pillar[1]
print(ans)