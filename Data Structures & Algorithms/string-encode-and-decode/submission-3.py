class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for word in strs:
            for i in word:
                encode = encode + "*" + i + "*"
            encode = encode + "#"
        return encode
           

        
    def decode(self, s: str) -> List[str]:
        words = []
        word = ""
        i = 0
        while i < len(s):
            if s[i] == "#":
                words.append(word)
                word = ""
                i += 1
            elif s[i] == "*":
                i += 1              # skip opening *
                word += s[i]
                i += 2              # skip char + closing *
        return words
 





