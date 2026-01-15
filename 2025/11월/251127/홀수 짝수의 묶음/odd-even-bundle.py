N = int(input())
'''
1. 최대 묶음 수를 만들어야 한다.
2. 모든 숫자가 사용되어야 한다.
3. 짝수의 개수는 항상 홀수와 같거나 -1 이다.

! 문제는 홀수 개수에 따라서 달라진다.


짝수와 홀수 개수가 동일하다면 -> 전체의 개수가 정답
짝수가 홀수보다 많다면 -> 홀수+2가 정답
홀수가 짝수보다 더 많이 있다면 ->
홀수로 짝수가 홀수보다 많아지도록 만들면 되겠구나!
'''
nums = list(map(int, input().split()))
even = []
odd = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

if len(odd) == len(even):
    print(len(nums))
elif len(even) > len(odd):
    print(len(odd)*2+1)
else:
    even_cnt = len(even)
    odd_cnt = len(odd)
    while odd_cnt > even_cnt:
        odd_cnt -= 2
        even_cnt += 1
    if odd_cnt == 0:
        print(1)
    elif odd_cnt == even_cnt:
        print(even_cnt*2)
    else:
        print(odd_cnt*2+1)