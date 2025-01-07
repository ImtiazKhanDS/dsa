# @leet start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n

        def findSlope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x2 - x1 == 0:
                return float("inf")
            else:
                return (y2 - y1) / (x2 - x1)

        ans = 1
        for i, p1 in enumerate(points):
            slopes = defaultdict(int)
            for p2 in points[i + 1 :]:
                slope = findSlope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans + 1

