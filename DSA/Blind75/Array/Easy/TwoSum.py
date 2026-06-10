# Problem Setup:
l1 = [9, 1, 5, 4, 7]
Target: 10

# Expected Output: [0, 1]
def twoSum(l1, target):
   seen = {} # Hashing for fast lookup
   for i in range(len(l1)):
       complement = target - l1[i]
       if complement in seen:
           return [i, seen[complement]]
       seen[l1[i]] = i


print(twoSum([9, 1, 5, 4, 7], 10)) # O(n) Efficiency