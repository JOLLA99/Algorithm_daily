def solution(s):
    # 문자열 리스트 처리
    half_s = len(s) // 2
    answer_list = []
    
    for n in range(1, half_s+1):
        #String 나누기
        div_list = [s[i:i+n] for i in range(0, len(s), n)]
        dup_list = [[1, div_list.pop(0)]]
        
        while div_list:
            sv = div_list.pop(0)
            if sv == dup_list[len(dup_list)-1][1]:
                dup_list[len(dup_list)-1][0] +=1
            else:
                dup_list.append([1, sv])
        
        answer= ''
        
        for i in range(0, len(dup_list)):
            if dup_list[i][0] == 1:
                answer += dup_list[i][1]
            else:
                answer += str(dup_list[i][0]) + dup_list[i][1]
        answer_list.append(len(answer))
        
    return min(answer_list)
                
