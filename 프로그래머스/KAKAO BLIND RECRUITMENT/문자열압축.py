def solution(s):
    answer = len(s)
    for index in range(1, int(len(s)/2)+1):
        cnt,length = 1,0
        comp = ""
        for i in range(0, len(s), index):
            base = s[i:i+index]
            if comp == base:
                cnt += 1
            elif comp != base:
                length += len(base)
                if cnt > 1:
                    length += len("{}".format(cnt))
                cnt = 1
                comp = base
        if cnt > 1:
            length += len("{}".format(cnt))
        answer = min(answer, length)
    return answer
