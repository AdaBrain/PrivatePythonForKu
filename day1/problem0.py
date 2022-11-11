nums = input()
nums = nums.split(" ")
if len(nums) == 2:
    result = int(nums[0]) + int(nums[1])
    print(result)
else:
    print("Error 0912: something wrong!")