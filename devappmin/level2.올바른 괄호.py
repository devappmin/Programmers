from collections import deque

def solution(s):
    q = deque()

    for t in s:
        if t == ')':
            if not len(q):
                return False

            q.pop()
            continue

        q.append('(')

    return True if not q else False

# Test Case
test_cases = [
                ["()()"],
                ["(())()"],
                [")()("],
                ["(()("],
            ]
test_cases_answer = [True, True, False, False]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
