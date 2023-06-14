import math
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallest_manDis = math.inf
        smallest_manDis_idx = 0
        for idx in range(len(points)):
            if x == points[idx][0] or y == points[idx][1]:
                manDis = (abs(points[idx][0]-x)+abs(points[idx][1]-y))
                if manDis < smallest_manDis:
                    smallest_manDis = manDis
                    smallest_manDis_idx = idx
        return -1 if smallest_manDis == math.inf else smallest_manDis_idx

                

                