class Solution:
    def decodeString(self, s: str) -> str:
        def dec(left):
            num=""
            chars=[]
            while left<len(s):
                if s[left]=="[":
                    letter,p=dec(left+1)
                    chars.append("".join(letter)*int(num))
                    left=p
                    num=""
                elif s[left]=="]":
                    break
                elif s[left].isnumeric():
                    num+=s[left]
                else:
                    chars.append(s[left])
                left+=1
            return chars,left
        return "".join((dec(0)[0]))
