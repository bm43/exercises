import time

nums = [2,7,11,15,1,3,66]
# print(list(enumerate(nums)))
target=26
h=[]
def twoSum(nums, target):
    print(list(enumerate(nums)))
    for i,num in list(enumerate(nums)):
        if target-num in nums:
            h.append(i)
        else:
            pass
    return h

st=time.time()
print(twoSum(nums,target))
et=time.time()
print(et-st)
