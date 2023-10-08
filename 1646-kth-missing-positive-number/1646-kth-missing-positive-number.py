class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # if the kth missing is less than arr[0]
        if k <= arr[0] - 1:
            return k
        k -= arr[0] - 1

        # search kth missing between the array numbers
        for i in range(len(arr) - 1):
            # missing between arr[i] and arr[i + 1]
            curr_missing = arr[i + 1] - arr[i] - 1
            # if the kth missing is between
            # arr[i] and arr[i + 1] -> return it
            if k <= curr_missing:
                return arr[i] + k
            # otherwise, proceed further
            k -= curr_missing

        # if the missing number if greater than arr[-1]
        return arr[-1] + k

# Time complexity O(N)
# Space complexity O(1)