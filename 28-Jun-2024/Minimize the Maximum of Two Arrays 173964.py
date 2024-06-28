# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        lcm = (divisor1 * divisor2) // gcd(divisor1,divisor2)
        
        def helper(mid):
            div1 = mid - mid//divisor1
            div2 = mid - mid//divisor2
            common = mid - mid//lcm
            return div1 >= uniqueCnt1 and div2 >= uniqueCnt2 and common >= (uniqueCnt1 + uniqueCnt2)
        
        left, right, best = 0, 10**11, float("inf")

        while right >= left:
            mid = left + (right-left)//2
            if helper(mid):
                right = mid - 1
                best = mid
            else:
                left = mid + 1
        return best
