class Common:
    def permutations(self, arr):
        return self.permutations_foo(arr, [], 0, 1)

    def permutations_foo(self, arr, prefix, start, dist):
        permutations = []

        for i in range(start, len(arr)):
            if dist == 1:
                permutations += [prefix+[arr[i]]]
            else:
                permutations = self.merge_uniques(permutations, self.permutations_foo(arr, prefix+[arr[i]], i+1, dist-1))

        if dist == len(arr):
            return permutations
        else:
            return self.merge_uniques(permutations, self.permutations_foo(arr, prefix, start, dist+1))

    def merge_uniques(self, arr1, arr2):
        for x in arr2:
            if x not in arr1:
                arr1 += [x]

        return arr1

# When start = 0, dist = 1, prefix = []
    # Iterate from 0->5 and add the array item to your list of permutations

# When start = 0, dist = 2, prefix = []
    # Iterate from 0->5. Each item will be a prefix for...

    # When start = 1, dist = 1, prefix = [1]
        # Iterate from 1->5: this time we have a prefix, we'll add our
        # current item to the prefix ([1])
    # When start = 2, dist = 1, prefix = [2]
        # Iterate from 2->5, add the prefix of 2 to all items
    # Start = 3, dist = 1, prefix = [3]
    # ... etc

# When start = 0, dist = 3, prefix = []
    # Iterate from 0->5. Each item will be a prefix for...

    # When start = 1, dist = 2, prefix = [1]
        # Iterate from 1->5. Each item will be a prefix for...

        # When start = 2, dist = 1, prefix = [1,2]
            # Iterate from 2->5, adding each item to [1,2]
        # When start = 3, dist = 1, prefix = [1,2]
            # Iterate from 3->5, adding each item to [1,2]
        # ... etc

# ... etc


# It looks like this:
# [1], [2], [3], [4], [5]
# TAKE [1]
# [1,2], [1,2], [1,3], [1,4], [1,5]
# TAKE [2]
# [2,3], [2,4], [2,5]
# etc..
#
# TAKE [1,2]
# [1,2,3], [1,2,4], [1,2,5]
# TAKE [1,3]
# [1,3,4], [1,3,5]
# TAKE [1,4]
# [1,4,5]
#
# TAKE [1,3]
# etc