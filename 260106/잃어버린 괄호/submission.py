'''
260106.잃어버린 괄호.submission의 Docstring
최소로 만들기 위해서는?
-의 앞에는 작은 숫자, 뒤에는 큰 숫자가 와야 한다.
+와 -만으로 이루어져 있으니..
-가 여러개 있는 경우
(최소) - (최대)
최대 안에 -가 또 있다면
(최소) - (최소 - 최대)
최소 안에도 - 가 있다면
(최소 - 최대) - (최소 - 최대)
- 뒤에를 다 묶어버린다 그냥. 심플하게
다시 -가 나오면 다시 묶는다.
'''
command = input().split('-')
ans = 0
for i, com in enumerate(command):
    adder = com.split('+')
    tmp = 0
    for ad in adder:
        tmp += int(ad)
    if i == 0:
        ans += tmp
    else:
        ans -= tmp
print(ans)