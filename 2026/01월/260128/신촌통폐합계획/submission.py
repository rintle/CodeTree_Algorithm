'''
2026.01월.260128.신촌통폐합계획.submission의 Docstring
N개의 대학교가 하나의 학교로 통합됨.
N개의 대학교의 이름을 이어 붙여서 정해짐.
N개를 나열한 뒤..
1. s_i, s_j가 빈 문자열이 아닌 서로 다른 두 정수 i, j를 고른다.
2. s_i의 뒤에 s_j를 붙인다.
3. s_j를 빈 문자열로 바꾼다.

모든 과정이 끝난 후, 빈 문자열이 아닌 s_k가 하나 남게되며, 이게 통합된 학교의 이름이 된다.
python list를 쓰는게 아니고, 정말로 linked_list의 특징을 활용해야하는 문제였다.
'''
import sys
input = sys.stdin.readline
N = int(input())
S = ['']+[input().rstrip() for _ in range(N)]
nxt = [0] * (N+1)
tail = [i for i in range(N+1)]
start = 0
for _ in range(N-1):
    i, j = map(int, input().split())
    nxt[tail[i]] = j
    tail[i] = tail[j]
    start = i
ans = []
# print(nxt)
# print(tail)
for _ in range(N):
    # print(S[start])
    ans.append(S[start])
    start = nxt[start]
print(''.join(ans))