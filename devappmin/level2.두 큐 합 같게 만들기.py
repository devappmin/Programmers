from collections import deque

def solution_time_out(queue1, queue2):
    left_sum = sum(queue1)
    right_sum = sum(queue2)
    
    perfect = (left_sum + right_sum) // 2
    
    left_pointer, right_pointer = 0, 0
    left_length, right_length = len(queue1), len(queue2)
    answer = 0
    get_answer = False
    
    while left_pointer != left_length and right_pointer != right_length:
        if left_sum == perfect and right_sum == perfect:
            get_answer = True
            break
        
        if left_sum > perfect or right_pointer == left_length - 1:
            left_sum -= queue1[left_pointer]
            right_sum += queue1[left_pointer]
            queue2.append(queue1[left_pointer])
            right_length += 1
            left_pointer += 1
        elif left_sum < perfect or left_pointer == right_length - 1:
            left_sum += queue2[right_pointer]
            right_sum -= queue2[right_pointer]
            queue1.append(queue2[right_pointer])
            left_length += 1
            right_pointer += 1
        else:
            break
        
        answer += 1
        
    
    return answer if get_answer else -1
    from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    left_sum, right_sum = sum(queue1), sum(queue2)
    perfect = (left_sum + right_sum) // 2
    
    answer = 0
    get_answer = False
    
    for _ in range(3 * len(queue1)):
        if left_sum < right_sum:
            left_sum += queue2[0]
            right_sum -= queue2[0]
            queue1.append(queue2.popleft())
        elif left_sum > right_sum:
            left_sum -= queue1[0]
            right_sum += queue1[0]
            queue2.append(queue1.popleft())
        else:
            get_answer = True
            break
            
        answer += 1
        
    
    return answer if get_answer else -1
    

# Test Case
test_cases = [
                [[3, 2, 7, 2], [4, 6, 5, 1]],
                [[1, 2, 1, 2], [1, 10, 1, 2]],
                [[1, 1], [1, 5]]
            ]
test_cases_answer = [2, 7, -1]
import time
for idx in range(len(test_cases)):
    s_time = time.process_time_ns()
    answer = 0
    answer = solution(*test_cases[idx])
    e_time = time.process_time_ns()
    print("Output : ", answer)
    print("Answer : ", test_cases_answer[idx])
    print("PASS {}ms".format(( e_time - s_time ) / 1000000) if answer == test_cases_answer[idx] else "FAILED",end="\n\n")
