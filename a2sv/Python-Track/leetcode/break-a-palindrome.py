class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        chars=[i for i in palindrome]
        count=Counter(chars)
        s="abcdefghijklmnopqrstuvwxyz"
        if len(count)==1:
            if len(palindrome)==1:
                return ""
            if palindrome[0]=="a":
                chars[-1]="b"
            else:
                chars[0]="a"
            return "".join(chars)
        for i,let in enumerate (chars):
            for j,alpha in enumerate(s):
                if let>alpha:
                    chars[i]=alpha                   
                    if chars != chars[::-1]:
                        return "".join(chars)
                    else:
                        chars[i]=let
        chars[-1]=chr(ord(chars[-1])+1)
        return "".join(chars)
        