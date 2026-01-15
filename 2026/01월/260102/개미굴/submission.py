import sys
 
sys.setrecursionlimit(3000)  # 예시: 재귀 깊이 제한을 높임

from collections import deque
class Node:
    def __init__(self, food):
        self.food = food
        self.next = {}

    def curFood(self):
        return self.food
    
    def addNode(self, new_node):
        food_name = new_node.curFood()
        # print(food_name)
        if food_name not in self.next:
            # print(f'Add {food_name} in {self.food}')
            self.next[food_name] = new_node
    
start = Node('entry')

N = int(input())
for _ in range(N):
    dfs = input().split()
    dfs = dfs[1:]
    p = dfs[0]
    # p_node가 
    if p in start.next:
        p_node = start.next[p]
    else:
        p_node = Node(p)
        start.addNode(p_node)
    # print(p_node.next)
    for n in dfs[1:]:
        if n in p_node.next:
            n_node = p_node.next[n]
        else:
            n_node = Node(n)    
            p_node.addNode(n_node)
        p_node = n_node

ans = ''
def dfs(node, cnt):
    global ans
    # print(f"Cur pos: {node.food}, rank: {cnt}")
    # print(node.next)
    # 종료 조건
    if not node.next:
        return
    # return
    for k, v in sorted(node.next.items()):
        ans += '--'*cnt
        ans += f'{k}\n'
        # return
        dfs(v, cnt+1)

dfs(start,0)
print(ans)