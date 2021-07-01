#dial 부분을 문자열이니까 ['ABC','DEF'....]이런 식으로 하는게 더 괜찮았을 것 같다.
al = input()
dial = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S']
        , ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
cnt = 0
for i in al:
    for j in range(len(dial)):
        if i in dial[j]:
            cnt += (j+3)
print(cnt)
