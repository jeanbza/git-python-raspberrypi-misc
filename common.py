class Common:
    def permutations(self, arr):
        return self.permutations_foo(arr, 0)

    def permutations_foo(self, arr, start):
        permutations = []

        permutations.append(arr[start:])

        for i in arr[start:len(arr)-1]:
            permutations.append(arr[i:])

            if len(arr[i:]) > 1:
                permutations.append(self.permutations_foo(arr[i-1:], start+1))

        return permutations