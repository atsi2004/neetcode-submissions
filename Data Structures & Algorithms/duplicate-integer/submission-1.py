class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:  # iterate through array
            if num in seen:  # if element has been seen before
                return True  # it is duplicate
            seen.add(num)  # otherwise add to seen
        return False  # element is not duplicate
