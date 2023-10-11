class BrowserHistory:

    def __init__(self, homepage: str):
        self.queue = collections.deque()
        self.pos = 0
        self.forwad = 0
        self.queue.append(homepage)

    def visit(self, url: str) -> None:
        if len(self.queue) > self.pos + 1:
            self.queue[self.pos + 1] = url
        else:
            self.queue.append(url)
        self.pos += 1
        self.forwad = 0

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.pos:
                self.pos -= 1
                self.forwad += 1
            else:
                break
        return self.queue[self.pos]

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.forwad:
                self.pos += 1
                self.forwad -= 1
            else:
                break
        return self.queue[self.pos]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)