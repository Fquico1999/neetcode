"""
Difficulty: Easy

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.
"""

class Solution:
    """
    Solution Class
    """
    def merge_old(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        #Check if empty
        if n==0:
            return
        if m == 0:
            for i, elem in enumerate(nums2):
                nums1[i] = elem
            return

        i = m-1 # nums1 pointer
        j = n-1 # nums2 pointer
        k = m+n-1 # overall
        while k >= 0:
            if i < 0:
                while j >= 0:
                    nums1[k] = nums2[j]
                    j-=1
                    k-=1
                break
            if j < 0:
                while i >= 0:
                    nums1[k] = nums1[i]
                    i-=1
                    k-=1
                break
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1

    def merge(self, nums1, m, nums2, n):
        i = m-1
        j = n-1
        k = m+n-1

        while j>=0:

            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1


if __name__ == "__main__":

    test1 = Solution()
    t = [1,2,3,0,0,0]
    test1.merge(t, 3, [2,5,6],3)
    assert t == [1,2,2,3,5,6], "Wrong"

    t = [0]
    test1.merge(t, 0, [1], 1)
    assert t == [1], "Wrong"

    t = [1]
    test1.merge(t, 1, [], 0)
    assert t == [1], "Wrong"

    t = [4,5,6,0,0,0]
    test1.merge(t, 3, [1,2,3],3)
    assert t == [1,2,3,4,5,6], "Wrong"

    t=[-1,0,0,3,3,3,0,0,0]
    test1.merge(t, 6, [1,2,2],3)
    assert t == [-1,0,0,1,2,2,3,3,3], "Wrong"

    t=[4,0,0,0,0,0]
    test1.merge(t, 1, [1,2,3,5,6],5)
    assert t == [1,2,3,4,5,6], "Wrong"

    t = [2,0]
    test1.merge(t,1,[1],1 )
    assert t == [1,2], "Wrong"
