class TimeMap:
    """
    Timestamps will always be monotonic, hence searching over them can be
    really fast. How do you search the time closest to called time

    Say 7 is called, 
    [1, 3, 11, 12] are previously logged times,
    then we need to quickly search for 7 in the list, or remember the closest
    small value
    """

    def __init__(self):
        self.hashmap = defaultdict(list)
        #self.hashdict = defaultdict(str)
        #name mapped to list of tuple (time, val)?
    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashmap[key]

        l, r = 0, len(arr) - 1
        res = (0, "")

        while l <= r:
            mid = (l + r)//2
            time, val = arr[mid]

            if time <= timestamp:
                res = (time, val)
                l = mid + 1
            else:
                r = mid - 1
        return res[1]
