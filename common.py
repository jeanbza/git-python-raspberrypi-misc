class Common:
    def permutations(self, arr):
        return self.permutations_foo(arr, 0, 3)

    def permutations_foo(self, arr, start, dist):
        permutations = []

        print "i j d l res"

        for i in range(len(arr)):
            for j in range(len(arr)-i-dist+1):
                j += i+dist-1

                res = arr[i:i+dist-1]+[arr[j]]

                print i, j, dist, len(arr), res

                if i+dist <= len(arr):
                    permutations.append(res)

        # if (start < len(arr)):
        #     permutations.append(self.permutations_foo(arr, start+1, dist))

        # if (dist < len(arr)):
        #     permutations += self.permutations_foo(arr, start, dist+1)

        return permutations
