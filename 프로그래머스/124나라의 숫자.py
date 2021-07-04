def solution(n):    # 10진법을 3진법과 비슷하게 변환해주는 알고리즘
    answer= ''
    
    while n > 0:  # 자연수
        n, mod = divmod(n, 3)
        if mod == 0:  # 나머지가 0 일 때는 4로 변환해주고 몫에 -1해준다.
            n -= 1   
            mod = 4
            answer += str(mod)  
        else:
            answer += str(mod)
           
    return answer[::-1]  # 역순인 진수를 뒤집어 줘야 제대로 출력
