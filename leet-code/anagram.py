"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ['ate', 'eat','tea'],
  ['nat','tan'],
  ['bat']
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
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