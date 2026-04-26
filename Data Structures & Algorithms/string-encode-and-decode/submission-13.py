class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "|"
        
        return encoded + ":" + "".join(strs)


    def decode(self, s: str) -> List[str]:
        break_point = 0
        for i, char in enumerate(s):
            if char == ":":
                break_point = i
                break
        
        info = s[0:i].split("|")

        output = []

        for length in info:
            if not length:
                continue 
            output.append(s[break_point + 1:break_point + 1 + int(length)])
            break_point = break_point + int(length)
        
        return output


