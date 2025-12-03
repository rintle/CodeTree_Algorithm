N = int(input())
nums = list(map(int, input().split()))

nums.sort()

small = nums[:N]
large = nums[N:]
max_min = 100000001
for i in range(N):
    max_min = min(max_min, large[i]-small[i])
print(max_min)

'''
묶음의 차이가 최대..
가장 작은거 끼리 묶으면?
안됨.
2 5 7 9 10 15
2 15 -- 13
5 10 -- 5
7 9 -- 2
해도 안됨.

정렬을 하고, 반갈죽 한 뒤
2 5 7
9 10 15
위 아래로 매칭시키면?
2 9 -- 7
5 10 -- 5
7 15 -- 8
이건가?
근데 숫자차이가 엄청 크게 난다면
1 200 300 99999998 99999999 100000000
'''
