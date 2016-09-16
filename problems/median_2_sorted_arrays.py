class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) < len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        if not nums2:
            mid1 = len(nums1) / 2
            return (nums1[mid1 - 1] + nums1[mid1]) / 2.0 if len(nums1) % 2 == 0 else nums1[mid1]
        need_le = (len(nums1) + len(nums2)) / 2
        def have_le2(le2, i1): return le2 <= 0 or le2 <= len(nums2) and nums2[le2 - 1] <= nums1[i1]
        def have_ge2(le2, i1): return le2 >= len(nums2) or le2 >= 0 and nums2[le2] >= nums1[i1]
        lo1, hi1 = 0, len(nums1) - 1
        while lo1 <= hi1:
            mid1 = (lo1 + hi1) / 2
            if have_le2(need_le - mid1, mid1) and have_ge2(need_le - mid1, mid1):
                lo1 = mid1
                break
            elif not have_le2(need_le - mid1, mid1):
                lo1 = mid1 + 1
            else:
                hi1 = mid1 - 1
        def find_lm(nums1, i1, nums2):
            if (len(nums1) + len(nums2)) % 2 != 0:
                return hm
            def prev(nums, i): return nums[i - 1] if i > 0 else None
            return max(prev(nums1, i1), prev(nums2, need_le - i1))
        if lo1 < len(nums1) and have_le2(need_le - lo1, lo1) and have_ge2(need_le - lo1, lo1):
            hm = nums1[lo1]
            lm = find_lm(nums1, lo1, nums2)
        else:
            hm = nums2[need_le - lo1]
            lm = find_lm(nums2, need_le - lo1, nums1)
        return (lm + hm) / 2.0
