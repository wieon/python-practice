# leetcode-0001 Two Sum
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

# Method 1
# for, for
# Python, Time 2136ms, Memory 13.07MB
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens = len(nums)
        for i in range(lens):
            res = lens-i-1
            for j in range(1, res+1):
                if nums[i] + nums[i+j] == target:
                    return [i, i+j]

# Method 2
# Hash table
# Time complex: O(N), Space complex: O(N)
# Python, Time 0ms, Memory 12.89MB
...
        hashtable = dict()  # hashtable is a dict, made up of key and value
        for i, num in enumerate(nums):
            res = target - num
            if res in hashtable:  # find key, not value; time complex is O(1)
                return [hashtable[res], i]  # i is always the last, haven't inserted in hashtable yet
            hashtable[nums[i]] = i  # hash function, build hash table
        return []
