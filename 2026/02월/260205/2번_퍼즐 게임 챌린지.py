'''
순서대로 n개의 퍼즐. 난이도와 시간 있음.
숙련도에 따라 틀리는 횟수 달라짐.
현재 난도 diff
소요 시간 time_cur
이전 시간 time_prev
내 숙련도 level
if diff <= level 
 time_cur
elif diff > level
 (diff - level)*(time_cur+time_prev) + time_cur
 
limit 안에 풀 수 있는 숙련도의 최소값?

길이는 3만.
모든 경우의 수를 할 수는 없다?
위에서 부터 줄여나가기? 너무 시간이 오래 걸린다.
level이 하나 정해졌을 때, 순회 최소 횟수: 300000 (30만)
diff의 크기 : 100000(10만)
30000000000 (300억, 불가능)
diff가 level보다 작으면? 그냥 time_cur이 필요함.
수식을 세울 수 있을까?
탐색 횟수를 줄여야 하는데. (level에 대한)
수식은 이렇게 세움 될 것 같다.
max(0, diff-level)*(time_cur + time_prev) + time_cur

diffs의 중간값부터 시작해서, 2진탐색으로 찾아가자. 이게 best 같다.
'''
def solution(diffs, times, limit):
    time_prev = -1
    time_cur = 0
    
    left = 1
    right = max(diffs)
    level = (right-left)//2
    len_N = len(diffs)
    perfect_level = -1
    while left <= right:
        level = (left+right)//2
        time = times[0]
        time_prev = time
        for i in range(1,len_N):
            time_cur = times[i]
            time += max(0, diffs[i]-level)*(time_cur+time_prev)+time_cur
            time_prev = time_cur
        # print(f"sum_time: {time}")
        # print(f"cur_left : {left}")
        # print(f"cur_level: {level}")
        # print(f'cur_right: {right}')

        # 현재 시간이 limit안에 들어온다면
        # level을 더 줄여야함.
        # 줄인 레벨로 이진탐색
        if time <= limit:
            perfect_level = level
            # print(f"level_down")
            right = level - 1
        # 현재 시간이 limit에 안들어오면
        # level을 올려야함
        # 올린 레벨로 이진탐색
        else:
            # print(f"level_up")
            left = level+1
        # breakpoint()
            
    return perfect_level