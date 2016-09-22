class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 9:59 - 10:08
        maxleft = [0]
        for h in height:
            maxleft.append(max(maxleft[-1], h))
        maxright, water = 0, 0
        for i in xrange(len(height) - 1, -1, -1):
            wall = min(maxleft[i], maxright)
            if wall > height[i]:
                water += wall - height[i]
            maxright = max(maxright, height[i])
        return water
