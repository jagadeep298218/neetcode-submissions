class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            for c in word:
                encoded += ("!" + c)
            encoded += "*"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        word = ""
        while len(s) > 0:
            if s[0] == "!":
                word += s[1]
                s = s[2:]
            elif s[0] == "*":
                decoded.append(word)
                word = ""
                s = s[1:]
        return decoded 
