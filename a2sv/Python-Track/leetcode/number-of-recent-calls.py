class RecentCounter:

    def __init__(self):
        self.counter=[]
        self.i=0

    def ping(self, t: int) -> int:
        self.counter.append(t)
        while self.counter[self.i]<t-3000:
            self.i+=1
        return len(self.counter)-self.i


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)