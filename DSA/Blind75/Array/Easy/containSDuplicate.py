def containsDuplicate(nums):
    if len(set(nums)) == len(nums):
        return False
    else:
        return True
    
nums = [1,2,3,4,5,6,5]
print(containsDuplicate(nums))