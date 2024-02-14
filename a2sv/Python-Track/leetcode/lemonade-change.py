class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        twenty=0
        for i in range(len(bills)):
            if bills[i]==5:
                five+=1
            elif bills[i]==10:
                if five>=1:
                    five-=1
                    ten+=1
                else:
                    return False
            else:
                if ten>=1 and five>=1:
                    ten-=1
                    five-=1
                    twenty+=1
                elif five>=3:
                    twenty+=1
                    five-=3
                else:
                    return False
        return True