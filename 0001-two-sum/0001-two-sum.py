class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                res = nums[i] + nums[j]

                if res == target:
                    return [i, j]

        return []