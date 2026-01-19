class HitCounter:

    def __init__(self):
        self.timestamps = []
        self.l = 0

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)
        self.l += 1

    def getHits(self, timestamp: int) -> int:
        
        l, r = 0, len(self.timestamps) - 1
        target = timestamp - 300

        #if timestamps isnt empty and latest value is beyond our not greater than target, return 0
        if not self.timestamps:
            return 0
        if self.timestamps and self.timestamps[-1] <= target:
            return 0

        index = r
        while l <= r:

            mid = l + (r - l) // 2

            if self.timestamps[mid] > target:
                r = mid - 1
                index = mid
            else:
                l = mid + 1

        return len(self.timestamps) - index


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)