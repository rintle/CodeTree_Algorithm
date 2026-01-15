'''
251215.색종이만들기.submission의 Docstring
현재 크기에 맞는 사각형이라면 - 그대로 return.
그렇지 않다면 - 4등분 해서 동일 작업 진행
'''
N = int(input())
grid = [list(map(int, input().split()))for _ in range(N)]

def isSquare(x, y, size):
    # 첫 크기가 사각인지 확인
    target = grid[x][y]
    notSquare = False
    for i in range(x, x+size):
        for j in range(y, y+size):
            if target != grid[i][j]:
                notSquare = True
                break
        if notSquare:
            break
    
    if not notSquare:
        if target:
            return 0, 1
        else:
            return 1, 0
    w, b = 0, 0
    # 그 다음은 4분위로 나누기
    q1_w, q1_b = isSquare(x, y, size//2)
    q2_w, q2_b = isSquare(x, y + size//2, size//2)
    q3_w, q3_b = isSquare(x + size//2, y, size//2)
    q4_w, q4_b = isSquare(x + size//2, y + size//2, size//2)
    w = q1_w+q2_w+q3_w+q4_w
    b = q1_b+q2_b+q3_b+q4_b
    return w, b

w, b = isSquare(0, 0, N)

print(w)
print(b)