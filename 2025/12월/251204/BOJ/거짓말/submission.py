# 그래프 문제구나. 14:41 깨달음
from collections import deque
N, M = map(int, input().split())
truth = input().split()

grid = [[0 for _ in range(N+1)]for _ in range(N+1)]
if len(truth) == 1:
    # 진실을 아는 사람이 없음
    print(M)
else:
    # 우선 모든 사람을 인접행렬에 위치시켜야함
    # 그 다음에, 사실을 아는 사람들의 수를 BFS로 탐색
    # 전체 - BFS 탐색 결과가 정답이 될 것
    ans = 0
    truth_people = map(int, truth[1:])
    party_list = []
    for _ in range(M):
        party = list(map(int, input().split()))
        cnt, party = party[0], party[1:]
        party_list.append(party)

        for i in range(cnt):
            grid[party[i]][party[i]] = 1
            for j in range(1, cnt):
                grid[party[i]][party[j]] = 1
                grid[party[j]][party[i]] = 1
    
    know_truth = [False for _ in range(N+1)]
    for p in truth_people:
        # BFS(p)
        q = deque()
        q.append(p)
        know_truth[p] = True
        while q:
            cur = q.popleft()
            for next in range(1, N+1):
                if not know_truth[next] and grid[cur][next]:
                    q.append(next)
                    know_truth[next]=True

    ans = 0
    for party in party_list:
        speak = True
        for p in party:
            if know_truth[p]:
                speak = False
                break
        if speak:
            ans += 1

    print(ans)