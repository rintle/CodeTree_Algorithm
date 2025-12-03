'''
A, B, C, A+B, B+C, C+A, A+B+C
일단 SORT해서, 가장 작은거 2개는 A와 B다.
그러면 숫자 3개가 빠진다
A, B, A+B
A+B+C가 가장 큰 숫자일 것이기 때문에
큰수 - (A+B) = C
'''
nums = list(map(int, input().split()))
nums.sort()
A, B = nums[0], nums[1]
C = nums[-1] - (A + B)
print(A, B, C)
