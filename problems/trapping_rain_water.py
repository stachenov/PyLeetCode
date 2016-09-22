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

    def trap_2pointers(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxleft, maxright = 0, 0
        i, j = 0, len(height) - 1
        water = 0
        while i <= j:
            maxleft = max(maxleft, height[i])
            maxright = max(maxright, height[j])
            if maxleft < maxright:
                if height[i] < maxleft:
                    water += maxleft - height[i]
                i += 1
            else:
                if height[j] < maxright:
                    water += maxright - height[j]
                j -= 1
        return water
