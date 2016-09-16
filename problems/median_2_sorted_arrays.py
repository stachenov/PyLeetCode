class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i1, i2 = find_medians(nums1, nums2)
        hm = min(get(nums1, i1), get(nums2, i2))
        if (len(nums1) + len(nums2)) % 2 != 0:
            return hm
        lm = max(get(nums1, i1 - 1), get(nums2, i2 - 1))
        return (lm + hm) / 2.0


def find_medians(nums1, nums2):
    need_less_or_equal = (len(nums1) + len(nums2)) / 2
    lo1, hi1 = 0, len(nums1) - 1
    while lo1 <= hi1:
        mid1 = (lo1 + hi1) / 2
        i2 = need_less_or_equal - mid1
        if get(nums2, i2 - 1) <= nums1[mid1] <= get(nums2, i2):
            lo1 = mid1
            break
        elif get(nums2, i2 - 1) > nums1[mid1]:
            lo1 = mid1 + 1
        else:
            hi1 = mid1 - 1
    return lo1, need_less_or_equal - lo1


def get(nums, i):
    if 0 <= i < len(nums):
        return nums[i]
    else:
        return float('-inf') if i < 0 else float('+inf')
