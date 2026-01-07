'''
260107.물 주기.submission의 Docstring
N개의 화분에 캣닢이 하나씩.
초기에 K만큼의 수분 머금고 있음
1. 연속된 A개의 화분에 물을 준다. - 수분 B만큼 증가
2. 모든 화분의 수분 1씩 감소
3. 수분이 0이 된 화분의 캣닢은 죽는다.
A가 N보다 작은 약수이므로, 무조건 캣닢은 죽게 되어 있다.
어떻게 가장 오래 살 수 있도록 캣닢을 유지할 수 있을까?
A가 N에 대해 딱 나눠떨어지는 수기 때문에, 앞에서 부터 그냥 차근차근 물을 준다.
예) N이 5라면, A는 무조건 1이다. 주다가 보면 죽게 되어있다.

'''
N, K, A, B = map(int,input().split())
plant = [K for _ in range(N)]

def watering(start, end):
    for i in range(start, end):
        plant[i] += B

def drying():
    for i in range(N):
        plant[i] -= 1

def check():
    if 0 in plant:
        return False
    return True
day = 0
idx = 0
while check():
    watering(idx, idx+A)
    idx = (idx+A)%N
    drying()
    day += 1
print(day)