def groupSum(start, nums, target):
    if start >= len(nums):  # constant
        return target == 0  # constant
    else:
        return groupSum(start + 1, nums, target - nums[start]) or groupSum(start + 1, nums, target)
        # __________________constant + T(n-1)___________________________constant+T(n-1)
    #   T(n) = T(n-1) + T(n-1)
    #   T(n) c1*2^(n-1)
    #   O(c1*2^(n-1)) O definition
    #   O(2^(n-1)) product rule
    #   O(2^n) sum rule
    #   Complexity in the worst case: O(2^n)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(groupSum(0, arr, 20))
