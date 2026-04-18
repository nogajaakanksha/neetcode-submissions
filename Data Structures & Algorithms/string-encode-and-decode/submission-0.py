class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ""
        
        # ['Hello', 'World'] --> 5,5,$HelloWorld
        res = ""
        # find the length of each string and append in res
        for s in strs:
            res += str(len(s)) + ","
        res += "$"

        for s in strs:
            res += s

        return res


    def decode(self, s: str) -> List[str]:

        if not s:
            return []
        
        res, sizes, i = [], [], 0
        while s[i] != "$":
            curr_s = ""
            while s[i] != ',':
                curr_s += s[i]
                i += 1
            sizes.append(int(curr_s))
            i += 1
        i += 1

        for size in sizes:
            res.append(s[i:i+size])
            i += size
        
        return res
