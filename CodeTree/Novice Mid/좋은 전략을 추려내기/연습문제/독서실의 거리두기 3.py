
# N = int(input())
# seats = list(map(int, list(input())))

def solution(N, seats):
    seats = list(map(int, list(seats)))
    longest = 0

    left = 0
    # find the longest two person
    cnt = 0
    for i in range(1,N):
        cnt += 1
        if seats[i]:
            # check if the two longest two people
            if longest < cnt:
                longest = cnt
                left = i-longest
            cnt = 0
    
    seats[left+longest//2] = 1
    # find the shortest two person

    
    cnt = 0
    shortest = 1000
    for i in range(1, N):
        cnt += 1
        if seats[i]:
            # check if the two shortest two people
            if shortest > cnt:
                shortest = cnt
            cnt = 0
    print(shortest)
solution(12,'100010010001')