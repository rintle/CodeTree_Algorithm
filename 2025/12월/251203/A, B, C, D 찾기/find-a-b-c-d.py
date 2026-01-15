'''
A, B, C, D
A+B B+C C+D D+A
A+B+C A+B+D A+C+D B+C+D
A+B+C+D
일단 제일 큰거 A+B+C+D
제일 작은거 A
순서가 이렇게 되겠네
A, B, C, A+B
'''
nums = list(map(int, input().split()))
nums.sort()
A = nums[0]
B = nums[1]
C = nums[2]
D = nums[-1] - (A+B+C)
print(A, B, C, D)