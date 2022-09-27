'''
Remove Duplicates from a list
'''
nums = [1,1,2]
n = set(nums)
nums = list(n)
nums.sort()
k = len(n)

print(k,nums)
    
