'''
260114.배열 합치기.submission의 Docstring
이미 정렬이 되어 있으니까, 순서대로 쭈욱 순회하면서, 더 작은걸 출력한다.
'''
lenA, lenB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a, b = 0, 0
ans = []
while a < lenA or b < lenB:
    if a >= lenA:
        ans.append(str(B[b]))
        b += 1
    elif b >= lenB:
        ans.append(str(A[a]))
        a += 1
    elif A[a] < B[b]:
        ans.append(str(A[a]))
        a += 1
    else:
        ans.append(str(B[b]))
        b += 1
print(' '.join(ans))