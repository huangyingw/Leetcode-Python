# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import fractions


class Solution:
    def maxPoints(self, points):
        if len(points) <= 2: return len(points)
        result = 0
        for i in range(len(points)):
            d = {}
            overlap = 0
            curmax = 0
            for j in range(i + 1, len(points)):
                dx = points[j].x - points[i].x
                dy = points[j].y - points[i].y
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                gcd = fractions.gcd(dx, dy)
                dx /= gcd
                dy /= gcd
                d[(dx, dy)] = d.get((dx, dy), 0) + 1
                curmax = max(curmax, d[(dx, dy)])
            result = max(result, curmax + overlap + 1)
        return result

