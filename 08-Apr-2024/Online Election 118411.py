# Problem: Online Election - https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons=persons
        self.times=times
        self.mydict=defaultdict(int)
        self.count=[]
        max_=0
        for i in range(len(persons)):
            self.mydict[persons[i]]+=1
            if self.mydict[persons[i]]>=self.mydict[max_]:
                self.count.append(persons[i])
                max_=persons[i]
            else:
                self.count.append(max_)

    def q(self, t: int) -> int:
        vote=bisect_left(self.times,t)
        if vote==len(self.times):
            return self.count[-1]
        if self.times[vote]==t:
            return self.count[vote]
        return self.count[vote-1]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)