"""
Problem: https://leetcode.com/problems/ransom-note

Description:
Given two strings, ransomNote and magazine, return whether ransomNote can be
constructed using letters from magazine. Each letter in magazine can only be
used once.

Approach:
Use a hashmap to count how many copies of each character ransomNote needs.

For each character in magazine, decrease its remaining count if it is still
needed. Remove a character once its count reaches zero. An empty hashmap means
all required characters were found.

Time complexity: O(n + m), where n and m are the lengths of the two strings.
Space complexity: O(k), where k is the number of distinct ransomNote characters
(at most 26 for lowercase English letters).
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = {}

        # Count how many copies of each character are needed.
        for char in ransomNote:
            if char in hashMap:
                hashMap[char] = hashMap[char] + 1
            else:
                hashMap[char] = 1

        # Use each magazine character to satisfy one remaining occurrence.
        for char in magazine:
            if char in hashMap:
                hashMap[char] = hashMap[char] - 1

                if hashMap[char] == 0:
                    # Stop tracking characters whose required count is satisfied.
                    hashMap.pop(char)

        # Any remaining character still needs more copies from magazine.
        if len(hashMap) == 0:
            return True

        return False
