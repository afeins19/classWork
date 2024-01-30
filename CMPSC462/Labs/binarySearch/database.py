"""
    - class student
        - Student_ID
        - first_name
        - last_name
        - email
        - major

        @TODO
        - implement time difference function
        - write time to end of text file
"""

import json
import math
import sys
import time
import random
import timeit
from prettytable import PrettyTable

class Database:
    def __init__(self, db_name, data=list):
        self.file = self.create_database(db_name, data)
        self.db_name = db_name

        #tracks times of sorting...takes in an entry with key=algorithm name, v=time taken to sort
        self.sort_times=dict()
    def create_database(self, db_name: str, data):
        with open(db_name, "w") as file:
            for obj in data:
                file.write(json.dumps(obj) + "\n")
        return file

    def write_file(self, name, data):
        """used to write a sorted object to a file"""
        with open(name, "w") as file:
            for obj in data:
                file.write(json.dumps(obj) + "\n")

        return file

    def selection_sort(self, attr):
        """uses the selection sort algorithm to sort the data in the db based on a given attribute"""
        file_name = f"selection_sort[{self.db_name}]_sortedBy_[{attr}].txt"
        data = self.get_data()


        """Selection sort:
            1. traverse array
            2. find smallest element
            3. swap element with the lowest position
            4. reduce the search size of the array from the left by 1 
            5. repeat until search range is 0
        """
        for sorted_line in range((len(data))):
            mindex = sorted_line

            #this traverses the unsorted portion of the list and tries to find the index of the smallest element
            for i in range(sorted_line, len(data)):
                if data[i][attr] < data[mindex][attr]: #we are comparing the attribute of each dictionary object
                    mindex = i

            #after the traversal, mindex holds the index of the smallest item
            #so perform a swap
            data[sorted_line], data[mindex] = data[mindex], data[sorted_line]

        self.write_file(file_name, data)
        return data

    def insertion_sort(self, attr):
        """uses the insertion sort algorithm to sort the data in the db based on a given attribute"""
        file_name = f"insertion_sort[{self.db_name}]_sortedBy_[{attr}].txt"
        data = self.get_data()

        """Insertion sort: 
            1. traverse array
            2. if 2 elements being compared are not in order, swap the smaller element
            with those in the sorted part ot the list until its place is found
            3. expand the sorted line by 1
            4. continue until we have traversed the array
        """

        for sorted_line in range(1, len(data)):
            j = sorted_line
            while j > 0 and data[j - 1][attr] > data[j][attr]:
                data[j - 1], data[j] = data[j], data[j - 1]
                j -= 1

        self.write_file(file_name, data)
        return data

    def bubble_sort(self, attr):
        """uses the bubble sort algorithm to sort the data in the db based on a given attribute"""
        file_name = f"bubble_sort[{self.db_name}]_sortedBy_[{attr}].txt"
        data = self.get_data()

        """bubble sort:
            1. traverse the list until the len(data) - sorted_line 
            2. compare adjacent elements
            3. if n-1 item is greater than n item perform swap
            4. continue until we hit the sorted line
            5. increment sorted line by 1           
        """

        #iterate over array...sorted area is formed at the end
        for sorted_line in range(len(data)):
            for i in range(0, len(data)-sorted_line-1):
                if data[i][attr] > data[i+1][attr]:
                    data[i + 1], data[i] = data[i], data[i + 1]

        self.write_file(file_name, data)

        return data

    def merge_sort(self, attr):
        file_name = f"merge_sort[{self.db_name}]_sortedBy_[{attr}].txt"
        data = self.get_data()
        sorted_data = self.merge_sorter(data, attr)

        self.write_file(file_name, sorted_data)
        return sorted_data

    def merge_sorter(self, data, attr):
        """Recursive function to split the lists"""

        """Merge sort:
            1. continously divide the list into 2 equal sublists l,r until each sublist of length 1
            2. sort the sublists and recombine with its partner and call a sort function to merge those 2 lists back into one
            3. repeat util we have reassembled list back (done automatically through recursion)
        """
        if len(data) <= 1:
            return data

        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        l_sorted = self.merge_sorter(left, attr)
        r_sorted = self.merge_sorter(right, attr)


        return self.make_merge(l_sorted, r_sorted, attr)

    def make_merge(self, left_sublist, right_sublist, attr):
        """helper function...recieves subarrays down from the merging function and sorts them"""
        merged = []

        #indicie tracking
        l, r = 0, 0

        #first we compare elements from the sublists and select items to be placed into our fully merged output
        while l < len(left_sublist) and r < len(right_sublist):
            if left_sublist[l][attr] < right_sublist[r][attr]:
                merged.append(left_sublist[l])
                l += 1
            else:
                merged.append(right_sublist[r])
                r += 1

        #if items remain in any of these sublists, add them to the merged list
        while l < len(left_sublist):
            merged.append(left_sublist[l])
            l += 1

        #...emptying right sublist
        while r < len(right_sublist):
            merged.append(right_sublist[r])
            r += 1

        return merged


    def get_data(self):
        if self.file:
            with open(self.file.name, "r") as file:
                return [json.loads(line) for line in file.readlines()]
        else:
            return None

    def __str__(self):
        with open(self.db_name) as file:
            students = file.readlines()
            return str(students)


class Student:
    def __init__(self, student_ID=None, first_name=None, last_name=None, email=None, major=None):
        self.data = {
            "student_ID": student_ID,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "major": major
        }

        if student_ID is None:
            self.make_random()

    def make_random(self):

        first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "Daisy", "Ella", "Frank", "Grace", "Henry", "Isabel",
                       "Jack", "Katie", "Leo", "Mia", "Noah", "Olivia", "Paul", "Quinn", "Riley"]
        last_names = ["Doe", "Smith", "Johnson", "Brown", "White", "Black", "Green", "Gray", "Adams", "Baker", "Clark",
                      "Davis", "Evans", "Foster", "Garcia", "Harris", "Jackson", "King", "Lee", "Morris"]
        majors = ["CS", "BIO", "MATH", "PHYS", "HIST", "ENG", "CHEM", "PSYC", "SOC", "PHIL", "ECO", "MUS",
                         "ANTH", "ME", "EE"]

        #generating the random attributes
        s_id = ''.join(random.choices('0123456789', k=9))
        s_fName = random.choice(first_names)
        s_lName = random.choice(last_names)
        s_major = random.choice(majors)
        s_email = f"{s_fName.lower()[0:2]}{s_lName.lower()[0]}{''.join(random.choices('0123456789', k=4))}@psu.edu"

        self.__init__(s_id, s_fName, s_lName, s_email, s_major)
    def __repr__(self):
        return self.data
    def __str__(self):
        return str(self.data)


# main section
def make_stats(function_to_call, *args, num=1):
    """takes in a function and can run it num-times"""
    time = timeit.timeit(lambda: function_to_call(*args), number=num)
    return time / num

# generating 20 random student objects (random because params are none)
students = [Student().__repr__() for i in range(2000)]


# creating a database and populating
test_db = Database("student_db", students)

sort_attrs = ['student_ID', 'first_name']
results = []

for attr in sort_attrs:
    out = {attr: {
            "insertion": make_stats(test_db.insertion_sort, attr, num=10),
            "selection": make_stats(test_db.insertion_sort, attr, num=10),
            "bubble": make_stats(test_db.insertion_sort, attr, num=10),
            "merge": make_stats(test_db.insertion_sort, attr, num=10)
        }}
    results.append(out)

#makes the output more readable by converting results into a string and then concatenating with \n
print("\n".join(map(str, results))+"\n\n")

id = list(list(results[0].values())[0].keys()) # sorry this is the way i formatted it
fname = list(list(results[1].values())[0].keys()) # sorry this is the way i formatted it

s_data = [list(item.values()) for item in list(list(results[0].values()))]  # This will give a list of lists
f_data = [list(item.values()) for item in list(list(results[1].values()))]

id_table = PrettyTable()
id_table.field_names = id

fname_table = PrettyTable()
fname_table.field_names = id

for row in s_data:
    id_table.add_row(row)

for row in f_data:
    fname_table.add_row(row)

print("Student_ID")
print(id_table, fname_table, sep="\n\nFirst Name:\n")

test_data = [random.randint(0, 10000) for _ in range(2000)]

msorted_data = test_db.merge_sorter(test_data)  # Assuming 'None' would mean sorting by value directly
isorted_data = test_db.insertion_sort(test_data)

