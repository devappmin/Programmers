def solution(A, B):
    A, B = sorted(A), sorted(B, key=lambda a: -a)

    answer = 0

    for a, b in zip(A, B):
        answer += a * b
    
    return answer

# Test Case
test_cases = [[[1, 4, 2], [5, 4, 4]], [[1, 2], [3, 4]]]
test_cases_answer = [29, 10]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
