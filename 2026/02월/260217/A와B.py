'''
Docstring for 2026.02월.260217.A와B
A와 B로만 이루어진 영어 단어가 존재함.
두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임.
다음 두 가지 연산만 가능함
문자열의 뒤에 A를 추가한다.
문자열을 뒤집고 B를 추가한다.

S를 T로 만들 수 있는지 없는지 알아낸다.
S를 T로 만드는게 아니고, T를 S로 만드는 것이 가능한 지를 파악한다!
'''
from collections import deque
S = deque(input())
T = deque(input())
reversed = False
while len(S) != len(T):
    if reversed:
        if T[0] == 'A':
            T.popleft()
        else:
            T.popleft()
            reversed = False
    else:    
        if T[-1] == 'A':
            T.pop()
        else:
            T.pop()
            reversed=True
if reversed:
    T.reverse()
same = True
while S:
    s = S.popleft()
    t = T.popleft()
    if s != t:
        same = False
        break
if same:
    print(1)
else:
    print(0)