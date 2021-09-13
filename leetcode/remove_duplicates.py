def remove_duplicates(nums):
    i = 0
    while i < len(nums)-1:
            # print("j=",j)
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i += 1
        
    # print(nums)
    return len(nums)

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,2,3,3,4]
print(remove_duplicates(nums2))
