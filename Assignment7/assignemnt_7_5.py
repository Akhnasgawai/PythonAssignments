def find_triplets_with_zero_sum(nums):
    triplets = []
    nums.sort()  # Sort the numbers in ascending order for efficient processing

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate elements in the outer loop

        left = i + 1
        right = len(nums) - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            if curr_sum == 0:
                triplets.append([nums[i], nums[left], nums[right]])

                # Skip duplicate elements in the inner loop
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                right -= 1

    return triplets


nums = [-1, 0, 1, 2, -1, -4]
triplets = find_triplets_with_zero_sum(nums)

for triplet in triplets:
    print(triplet)
