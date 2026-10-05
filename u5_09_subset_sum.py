def subset_sum(nums, target):
    nums = sorted(nums)
    found = []
    chosen = []

    def go(i, remaining):
        if remaining == 0:
            found.append(chosen[:])
            return

        if i == len(nums) or nums[i] > remaining:
            return

        # Choose nums[i]
        chosen.append(nums[i])
        go(i + 1, remaining - nums[i])
        chosen.pop()  # Backtrack

        # Skip nums[i]
        go(i + 1, remaining)

    go(0, target)

    return found


print("Solutions for [3, 34, 4, 12, 5, 2], target 9:")
print(subset_sum([3, 34, 4, 12, 5, 2], 9))

print()

print("Solutions for [1, 2, 3], target 7:")
print(subset_sum([1, 2, 3], 7))
def subset_sum(nums, target):
    nums = sorted(nums)
    found = []
    chosen = []

    def go(i, remaining):
        if remaining == 0:
            found.append(chosen[:])
            return

        if i == len(nums) or nums[i] > remaining:
            return

        # Choose nums[i]
        chosen.append(nums[i])
        go(i + 1, remaining - nums[i])
        chosen.pop()  # Backtrack

        # Skip nums[i]
        go(i + 1, remaining)

    go(0, target)
    return found


nums = [3, 34, 4, 12, 5, 2]
target = 15

print("Numbers:", nums)
print("Target:", target)
print("Subsets:", subset_sum(nums, target))
