from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map[key]

        if not values:
            return ""
        
        left = 0
        right = len(values) - 1

        while left <= right:
            # largest previous or equal timestamp
            mid = (left + right) // 2
            t = values[mid][1]

            if t > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        if values[right][1] <= timestamp:
            return values[right][0]
        return ""





