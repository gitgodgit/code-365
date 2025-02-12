class RecentCounter:

        def __init__(self):
            self.count = 0
            self.pingArray = deque()

        def ping(self, t: int) -> int:
            self.pingArray.append(t)
            while self.pingArray[0] < t - 3000:
                self.pingArray.popleft()
            return len(self.pingArray)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)