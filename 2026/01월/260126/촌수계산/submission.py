'''
2026.01월.260126.촌수계산.submission의 Docstring
가족, 친척들 사이 관계를 촌수라는 단위로 표현함.
부모-자식: 1촌
나와 할아버지 : 2촌
아버지 형제들과 할아버지는 1촌, 나와 아버지 형제는 3촌.
부모 자식 관계가 주어졌을 대, 주어진 두 사람의 촌수?

N의 연속된 번호로 각각 표시.
둘째줄에는 촌수 계산해야하는 번호 주어짐
셋째줄에는 부모-자식 관계의 개수 m이 주어짐.
넷째줄 부터는 x,y가 주어지는데, x는 y의 부모라는 뜻.


           할아버지
              │
┌─────────┬───┴───┬───────┐
삼촌1   삼촌2   삼촌3    아빠
                          │
                          나
이렇게 그리면 아빠랑 나랑 이어진것 같지만


나 - 아빠 - 할아버지 - 삼촌1
                     ㄴ삼촌2
                     ㄴ삼촌3
이렇게 그리면, 나-삼촌까지 촌수가 3촌인게 보인다.
그래프를 그리고, 촌수를 계산해야하는 번호까지 갈 수 있는지를 조사하면 된다.

'''
N = int(input())
a, b = map(int, input().split())
M = int(input())
matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1
def dfs(cur_no, cnt):
    visited[cur_no] = True
    if cur_no == b:
        return cnt
    rlt = -1
    for y in range(N+1):
        if matrix[cur_no][y] and not visited[y]:
            rlt = max(rlt, dfs(y, cnt+1))
    return rlt
print(dfs(a, 0))