from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    answer = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                answer.append(i)
                answer.append(j)
                break
    return answer