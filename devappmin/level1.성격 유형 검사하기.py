from collections import defaultdict

data = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]

def solution(surveies, choices):
    dicts = defaultdict(int)
    
    for survey, choice in zip(surveies, choices):
        first, second = survey
        
        if choice < 4:
            dicts[first] += 4 - choice
            continue
        
        if choice == 4:
            continue
            
        if choice > 4:
            dicts[second] += choice - 4
            continue
    
    answer = ''
    
    for left, right in data:
        if dicts[left] == dicts[right]:
            answer += min(left, right)
            continue
            
        answer += (left if dicts[left] > dicts[right] else right)
    
    return answer

# Test Case
test_cases = [
                [["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]],
                [["TR", "RT", "TR"], [7, 1, 3]]
            ]
test_cases_answer = [
    "TCMA", "RCJA"
]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
