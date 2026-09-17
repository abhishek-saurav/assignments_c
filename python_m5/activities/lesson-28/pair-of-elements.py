class pair_elements:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i

target = int(input("Enter target sum: "))
sol = pair_elements()
result = sol.twoSum((10, 20, 30, 40, 50, 60, 70), target)
print(f"Pair found at positions: {result[0]} and {result[1]}")
