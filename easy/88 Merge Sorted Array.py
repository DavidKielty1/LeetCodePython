class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        #Last index nums1
        last = m + n - 1

        #merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
                print(nums1)
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
                print(nums1)
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1
            print(nums1)


    merge(self='self', nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
    