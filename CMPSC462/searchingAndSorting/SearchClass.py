import math
class SearchClass:

    def sort_data(self, vals):
        vals = vals.sort()
        return vals

    def unique_values(self, data):
        data = sorted(data) # sort to check adjacent indicies
        dups=[]

        i=0
        while i < len(data)-2:
            if data[i] == data[i+1]:
                dups.append(data[i])

                # iterate i until we find the next unique val
                while data[i] == data[i+1] and i<len(data)-2:
                    i+=1

            else:
                i+=1
        if dups:
            print(f"{len(dups)} dups", dups)
            return False
        return True

    def linear_search(self, vals, target):
        for i in range(len(vals)):
            if vals[i] == target:
                return (target, i) # returns target and index within passed in pool
        return None

    def binary_search(self, vals, target):

        max_index = len(vals) - 1 # largest index in sorted vals
        min_index = 0 # index of first adn smallest element in sorted vals

        while min_index <= max_index:
            mid = math.floor((min_index+max_index)/2)

            if vals[mid] == target:
                return (target, mid)
            elif target > vals[mid]: # set min to mid+1
                min_index = mid + 1

            elif target < vals[mid]: # set max to mid-1
                max_index = mid - 1

        return None # if we don't find it return null

    def min(self, vals):
        min_val = vals[0]

        for val in vals:
            if val < min_val:
                min_val = val
        return min_val

    def max(self, vals):
        max_val = vals[0]

        for val in vals:
            if val > max_val:
                max_val = val
        return max_val