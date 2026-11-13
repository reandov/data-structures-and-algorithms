"""
Problem: https://leetcode.com/problems/two-sum

Description:
Given an array of integers and a target, return the indices of two distinct
integers where the sum of both is equal to target. This problem has at least
one solution. 

Approach: 
Use a hashmap to store the complement (target - num) of each visited number as
the key and it's index as the value.

For each number, check whether it's already present in the hashmap, it its
we found the whole sum and return the complement index and the current index.
Otherwise we just store the complement using the approach above.

Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]

            seen[num] = index

        raise ValueError("No valid pair found")