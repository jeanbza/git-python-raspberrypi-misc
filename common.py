class Common:
    def permutations(self, arr):
        return self.permutations_foo(arr, [], 0, 1)

    def permutations_foo(self, arr, prefix, start, dist):
        permutations = []

        for i in range(start, len(arr)):
            if dist == 1:
                permutations += [prefix+[arr[i]]]
            else:
                permutations += self.permutations_foo(arr, prefix+[arr[i]], i+1, dist-1)

        if dist == len(arr):
            return permutations
        else:
            return permutations + self.permutations_foo(arr, prefix, start, dist+1)