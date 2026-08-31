class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        nums.sort() # sorting array is n log n runtime

        for i in range(1,length):
            if nums[i] == nums[i-1]:
                return True
        return False