class Solution:
    def encode(self, strs: List[str]) -> str:
        '''
        we use a length + delimeter + actual string
        using += for strings is very inefficient
        '''
        return ''.join(f"{len(s)}${s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        while i < len(s):
            j = s.find("$",i)
            length = int(s[i:j])
            results.append(s[j+1:j+1+length])
            i = j+1+length
        return results
        