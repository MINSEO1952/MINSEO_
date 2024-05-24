# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 
# solution 함수를 완성해주세요.

from itertools import combinations

def solution(*nums):
    if len(nums) < 3:
        return "3개 이상의 값을 입력해주세요."
    
    if len(nums) == 3:
        total_sum = sum(nums)
        for i in range(2, total_sum):
            if total_sum % i == 0:
                return "소수가 아닙니다"
        else:
            return "소수입니다"
        
    else:
        count = 0
        com_length_3 = list(combinations(nums, 3))
        for com in com_length_3:
            for i in range(2, sum(com)):
                if sum(com) % i == 0:
                    break
            else:
                print(f"입력하신 값 중 {com}의 합인 {sum(com)}의 경우 소수입니다")
                count += 1
        
        return f"총 소수가 되는 경우는 {count} 가지입니다."

# 예제 호출
print(solution(1, 2, 3, 5,8))
