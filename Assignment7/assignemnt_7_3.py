li = [4, 5, 6]


class Subset:
    def find_subset(nums):
        subset = []
        result = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result


print(Subset.find_subset(li))
