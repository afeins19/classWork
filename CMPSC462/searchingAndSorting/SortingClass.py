import math


class SortingClass:

    def selection_sort(self, data):
        for i in range(len(data)): # fixed value to compare rest of list to
            for j in range(i+1,len(data)): # comparing all other elements to this one
                if data[j] < data[i]:
                    data[i], data[j] = data[j], data[i] #swap
        return data

    def insertion_sort(self, data):
        for i in range(len(data)-1): # defines sorted list
            if data[i+1] < data[i]:  # if the next target is smaller than current
                temp = data[i+1] # hold for shifting

                j=i
                while j >= 0 and data[j] > temp: # perform shifting until we find the correct spot in the sorted portion
                    data[j + 1] = data[j]
                    j -= 1
                data[j + 1] = temp # perform insertion
        return data
    def bubble_sort(self, data):
        for i in range(len(data)):
            for j in range(len(data)-i-1): # higher values bubble to top every pass so list becomes sorted right to left
                if data[j] > data[j+1]: # out of order
                    data[j], data[j+1] = data[j+1], data[j] # pefrom swap
        return data
    def merge_sort(self, data):
        #half the data until lists contain 1 target, then merge
        if len(data) == 1:
            return data
        else:
            # divide data into left and right halves
            mid = math.floor(len(data)/2)

            l = self.merge_sort(data[0:mid])
            r = self.merge_sort(data[mid:])

        return self.merge_handler(l,r)
    def merge_handler(self, l, r):
        merged = []
        i=0
        j=0

        #start recombining items from both lists
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                merged.append(l[i])
                i += 1
            else:
                merged.append(r[j])
                j += 1

       #empty this list if right list has been emptied
        while i < len(l):
            merged.append(l[i])
            i += 1

        #otherwise empty this list
        while j < len(r):
            merged.append(r[j])
            j += 1

        return merged