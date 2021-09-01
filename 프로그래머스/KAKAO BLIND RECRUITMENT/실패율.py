from collections import Counter
def solution(N, stages):
    l, c, answer = len(stages), Counter(stages),{}  
    for key in range(1,N+1):  # keys는 스테이지 개수 N 으로 알 수 있다. 
        if l != 0:  # stages길이는 1이상이라고 했지만, 0이 올 수도 있으니까 예외처리..
            pre_value = c[key]  # 각 스테이지 별 실패 건수 세기 
            answer[key] = pre_value / l  # 실패율을 value값으로 넣어준다.
            l = l-pre_value    # ex) {1:0.125, 2:0.428571, 3:0.5, 4:0.5, 5:0 }
        else:
            answer[key] = 0  #  만약 N = 2라면, {1:0,2:0}            
    return sorted(answer,key=lambda x:answer[x],reverse=True ) 

 ##########################################################################################################
  # 나는 사실 keys 값이 정해져있다는 것을 몰랐던 것이다..
  # collections Counter로도 충분히 풀 수 있다. 
 ##########################################################################################################