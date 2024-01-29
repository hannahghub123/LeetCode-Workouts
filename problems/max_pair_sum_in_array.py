'''2815. Max Pair Sum in an Array

You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the maximum digit in both numbers are equal.

Return the maximum sum or -1 if no such pair exists.

 

Example 1:

Input: nums = [51,71,17,24,42]
Output: 88
Explanation: 
For i = 1 and j = 2, nums[i] and nums[j] have equal maximum digits with a pair sum of 71 + 17 = 88. 
For i = 3 and j = 4, nums[i] and nums[j] have equal maximum digits with a pair sum of 24 + 42 = 66.
It can be shown that there are no other pairs with equal maximum digits, so the answer is 88.

Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: No pair exists in nums with equal maximum digits.
 '''

def max_sum_pair(nums):
    my_dict={}
    for i in range(len(nums)):
        max_digit = int(max(list(str(nums[i]))))
        if my_dict.get(max_digit):
            my_dict[max_digit].append(nums[i])
        else:
            my_dict[max_digit]=[]
            my_dict[max_digit].append(nums[i])
        
    pair_sum=-1
    for key,value in my_dict.items():

        if len(value)>2:
            value=sorted(value)
            if pair_sum<(value[-1]+value[-2]):
                pair_sum=value[-1]+value[-2]

        elif len(value)>1 and sum(value)>pair_sum:
            pair_sum=sum(value)
                

    return pair_sum


nums = [84,91,18,59,27,9,81,33,17,58]
print(max_sum_pair(nums))
