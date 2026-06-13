from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        we use frequency array on our anagarams and then group them
        together based on that
        '''
        
        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char)-ord('a')] += 1

            anagrams[tuple(count)].append(s)

        return list(anagrams.values())


        