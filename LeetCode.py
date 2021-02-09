class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needToFind = 0
        output = []
        for i in nums:
            needToFind = target - i
            if needToFind in nums[nums.index(i) + 1:]:
                output.append(nums.index(i))
                # nums2 = [nums.index(i)+1:]
                output.append(nums[nums.index(i) + 1:].index(needToFind) + nums.index(i) + 1)
                break

        return output