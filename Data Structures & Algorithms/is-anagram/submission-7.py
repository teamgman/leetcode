class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a1 = {}
        a2 = {}
        for e in s:
            if e in a1:
                a1[e] += 1
            else:
                a1[e] = 1

        for e in t:
            if e in a2:
                a2[e] += 1
            else:
                a2[e] = 1

        return a1 == a2