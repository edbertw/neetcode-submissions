"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # maximum number of overlapping intervals
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))
        # C1: [(3, -1), (3, 1)] --> (-1) + 1 signifies the previous meeting ends then a new one begins, so no overlapping

        times.sort(key=lambda x: (x[0], x[1]))

        res = 0
        cnt = 0

        for time in times:
            cnt += time[1]
            res = max(res, cnt)

        return res



        