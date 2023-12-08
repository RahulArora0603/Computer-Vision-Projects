class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list2 = []
        for i in range(0, len(nums)):
            for j in nums:
                if j==nums[i]:
                    continue
                elif (nums[i]+j)==target:
                    list1 = [nums.index(nums[i]), nums.index(j)]
                    print(f"{nums[i]},{j}")
                    list2.append(list1)
        return list2

arr = [1,2,3,4]
target1 = 5               
arr2 = twoSum(arr , target1)
print(arr2)