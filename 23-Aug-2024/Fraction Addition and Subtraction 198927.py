# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, s: str) -> str:
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        def calculate(a1, b1, a2, b2, lcm):
            a = lcm // b1 * a1
            b = lcm // b2 * a2
            return (a + b, lcm)

        arr = []
        i = 0
        temp = []
        s = "+" + s + "+"
        
        while i < len(s):
            if s[i] in "+-":
                if len(temp) < 3:
                    temp = []
                else:
                    idx = temp.index("/")
                    a = int("".join(temp[1:idx]))
                    b = int("".join(temp[idx + 1 :]))
                    if temp[0] == "-":
                        a = 0 - a
                    arr.append((a, b))
                    temp = []
            if s[i] not in "+-":
                temp.append(s[i])
            else:
                temp.append(s[i])
            i += 1

        a = 0
        b = 1
        for x, y in arr:
            Lcm = lcm(y, b)
            a, b = calculate(x, y, a, b, Lcm)

        if a == 0:
            return "0/1"

        # simplify
        d = 2
        for i in range(int(sqrt(max(a, b))) + 1):
            while a % d == 0 and b % d == 0:
                a //= d
                b //= d
            d += 1
        return f"{a}/{b}"
