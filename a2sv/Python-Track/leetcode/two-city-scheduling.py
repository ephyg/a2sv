class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        tot=[[(a-b),a,b]for a,b in costs]
        tot.sort()
        toA=[a[1] for a in tot[:len(tot)//2]]
        toB=[b[2] for b in tot[len(tot)//2:]]
        return sum(toA)+sum(toB)