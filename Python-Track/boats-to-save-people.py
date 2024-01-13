class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left=0
        right=len(people)-1
        counter=0
        while right>=left:
            s=people[right]+people[left]
            if s>limit:
                counter+=1
                right-=1
            elif s<=limit:
                counter+=1
                right-=1
                left+=1
        return counter
