'''
251215.쿼드트리.submission의 Docstring
색종이와 유사하지만, return을 어떻게 주고 어떻게 출력할 지 고민해야하는 문제
'''
N = int(input())
grid = [list(map(int, list(input()))) for _ in range(N)]

def quadTree(x, y, size, b_s, b_e):
    if b_s:
        print('(', end='')
    # 현재 size에 대해, 하나의 값으로 이뤄져있는지 확인
    target, allSame = grid[x][y], True

    for i in range(x, x+size):
        for j in range(y, y+size):
            if grid[i][j] != target:
                allSame = False
                break
        if not allSame:
            break

    if allSame:
        print(target, end='')
    else:
        # q1 quadtree
        quadTree(x, y, size//2, True, False)
        quadTree(x, y+size//2, size//2, False, False)
        quadTree(x+size//2, y, size//2, False, False)
        quadTree(x+size//2, y+size//2, size//2, False, True)
    if b_e:
        print(')', end='')

quadTree(0, 0, N, False, False)