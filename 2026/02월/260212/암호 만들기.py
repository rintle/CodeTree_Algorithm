'''
2026.02월.260212.암호 만들기의 Docstring

암호로 동작하는 시스템
서로다른 L개의 알파벳 소문자, 최소 1개의 모음 (aeiou)와 2개의 자음 (최소 3글자)
오름차순 배열
문자의 종류는 C가지.
가능한 암호를 모두 구하는 프로그램?
'''
from collections import deque
L, C = map(int, input().split())
letters = input().split()
letters.sort()
moum = 0
zaum = 0
answer = []
password = deque()
def code(idx, cnt):
    global moum, zaum, password
    if cnt == L:
        if moum >= 1 and zaum >= 2:
            answer.append(''.join(password))
            return
        return
    for i in range(idx, C):
        if letters[i] in ['a','e','i','o','u']:
            moum += 1
            password.append(letters[i])
            code(i+1, cnt+1)
            password.pop()
            moum -= 1
        else:
            zaum += 1
            password.append(letters[i])
            code(i+1, cnt+1)
            password.pop()
            zaum -= 1
    
code(0,0)
print('\n'.join(answer))