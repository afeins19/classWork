import random


def findKthLargest(nums: list[int], k: int) -> int:
    # partition the array into vals < pivot and > than pivot
    def partition(nums, l, r):
        pivot = nums[r]
        cur_idx = l

        # move numbers into place with respect to the pivot
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[cur_idx], nums[i] = nums[i], nums[cur_idx]
                cur_idx += 1

        nums[cur_idx], nums[r] = nums[r], nums[cur_idx]  # move pivot into place
        return cur_idx  # return index of pivot placement

    n = len(nums)
    l, r = 0, n - 1

    # order elements around the pivot in the partition
    while l <= r:
        pivot_idx = partition(nums, l, r)

        # pivot is our element -> return the element
        if pivot_idx == n - k:
            return nums[pivot_idx]

        # pivot < kth largest -> search right array
        elif pivot_idx < n - k:
            l = pivot_idx + 1

        # pivot_iex > kth largest -> search left array
        else:
            r = pivot_idx - 1


# testing
nums = random.sample(range(100), 10)

    # finding the kth largest element

# selecting an index in nums
k = random.randint(0, len(nums)-1)
print(f"K = {k}\n")

# testing output with sorting method
val_from_sorted = sorted(nums)[len(nums)-k]
print(f"Sorting: nums[k]={val_from_sorted}")

# testing quickselect
val_from_quickselect = findKthLargest(nums=nums, k=k)
print(f"Quickselect: nums[k]={val_from_quickselect}")