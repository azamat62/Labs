def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True
    return False           
print(has_33([3, 3, 2]))
