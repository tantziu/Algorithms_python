def rotate(nums, k):
    first = []
    second = []
    for i in range(len(nums)):
        if i <= k:
            second.append(nums[i])
        else:
            first.append(nums[i])
    return first+second

def rotate2(nums, k):
    n = len(nums)
    k %= n
    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)
    return nums


def reverse(a, start, end):
    i = 0
    while i <= (end-start) // 2:
        a[i+start], a[end-i] = a[end-i], a[i+start]
        # a[end-i] = a[i+start]
        i += 1
    return a


nums1 = [1,2,3,4,5,6,7] 
nums2 = [-1]
k = 3

print(rotate2(nums2, k))
# print(reverse(nums, 0, 6))