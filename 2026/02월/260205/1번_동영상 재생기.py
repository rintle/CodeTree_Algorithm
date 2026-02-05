'''
10초 전으로 이동
10초 후로 이동
오프닝 건너뛰기
'''
def m2s(x):
    m, s = map(int, x.split(':'))
    return 60*m+s
def s2m(x):
    m = x//60
    s = x%60
    return f"{m:02d}:{s:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len = m2s(video_len)
    pos = m2s(pos)
    op_start = m2s(op_start)
    op_end = m2s(op_end)
    
    if op_start <= pos <= op_end:
        pos = op_end
    for c in commands:
        if c == "prev":
            pos = max(0, pos-10)
        elif c == "next":
            pos = min(video_len, pos + 10)
        
        if op_start <= pos <= op_end:
            pos = op_end
    return s2m(pos)