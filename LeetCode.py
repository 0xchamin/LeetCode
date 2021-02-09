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


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if (x > 0):
            sign = 1
        elif (x < 0):
            sign = -1

        number = str(abs(x))
        charArr = list(number)
        reversedNum = int(''.join(reversed(charArr)))

        numToReturn = int(reversedNum) * sign

        if numToReturn not in range((-1 << 31), (1 << 31) - 1):
            return 0
        else:
            return numToReturn