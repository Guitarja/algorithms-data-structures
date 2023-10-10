class OrderedStream:

    def __init__(self, n: int):
        self.pos = 0
        self.buff = [""] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        temp_buff = []
        self.buff[idKey-1] = value
        while self.pos < len(self.buff) and self.buff[self.pos]:
            temp_buff.append(self.buff[self.pos])
            self.pos += 1
        return temp_buff

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)