"""
https://leetcode.com/problems/anagrams/
Given an array of strings, return all groups of strings that are anagrams.
"""
from collections import defaultdict
class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        groups = defaultdict(list)
        for word in strs:
            groups[''.join(sorted(word))].append(word)

        answer = []
        for group in groups.values():
            if len(group) > 1:
                answer.extend(group)
        return answer
