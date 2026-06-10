def moveZeroes(num):
    insert = 0 # position of the value zero in an array 
    for i in range(len(nums)):
       if nums[i] != 0:
           nums[i],nums[insert]=nums[insert],nums[i]
           insert += 1
    return nums

nums = [0,1,0,0,12]
print(moveZeroes(nums))

# TC : o(n)
# SC: o(1)