class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        our goal is to make sure we only calculate everything only once
        thus my idea is to have two arrays which track product of
        left side and right side of every index
        '''
        results = [1] * len(nums)

        total = 1
        for i in range(len(nums)):
            results[i] = total
            total *= nums[i]

        total = 1
        for i in reversed(range(len(nums))):
            results[i] *= total
            total *= nums[i]

        return results
        