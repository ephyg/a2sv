class BrowserHistory:

    def __init__(self, homepage: str):
        self.backStack=[homepage]
        self.forwardStack=[]
            


    def visit(self, url: str) -> None:
        self.backStack.append(url)
        self.forwardStack=[]

    def back(self, steps: int) -> str:
        for i in range(steps):
            if len(self.backStack)>1:
                x=self.backStack.pop()
                self.forwardStack.append(x)
        return self.backStack[-1] 

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.forwardStack:
                x=self.forwardStack.pop()
                self.backStack.append(x)  
        return self.backStack[-1] 

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)