def solution(N, stages):
    l, answer = len(stages), {}  # 이번에는 collections 말고 딕셔너리로
    for key in range(1,N+1):  # keys는 스테이지 개수 N 으로 알 수 있다. 
        if l != 0:  # stages길이는 1이상이라고 했지만, 0이 올 수도 있으니까 예외처리..
            pre_value = stages.count(key)  # 각 스테이지 별 실패 건수 세기 
            answer[key] = pre_value / l  # 실패율을 value값으로 넣어준다.
            l = l-pre_value    # ex) {1:0.125, 2:0.428571, 3:0.5, 4:0.5, 5:0 }
        else:
            answer[key] = 0  #  만약 N = 2라면, {1:0,2:0}    
    return sorted(answer,key=lambda x:answer[x],reverse=True )  

 ##########################################################################################################
 # 처음에는 collections의 Counter를 사용해 값이 있는 것만 실패율 구하고 나머지는 append하는 식으로 구했으나
 # 자꾸 테스트케이스 14번과 26번이 실패해서,, 이 문제는 다시 한번 고민해보는 걸로..   
 ##########################################################################################################