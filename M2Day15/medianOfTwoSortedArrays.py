def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1 + nums2))