"""2. Create a database with the following details for at least 20 students and store it as a text file:
 Student ID
 first name
 last name
 email id
 Major
 Write a program to read the data from the text file. Choose an appropriate data type and data
structure (lists, lists of list, dictionary) for storing the information in your program.


 Write a function which takes a parameter and sorts the entire list of students and displays all the
details of all students. Your function should sort the list using student id or first name or last name.
Implement the sorting using selection sort, insertion sort, bubble sort and merge sort, and print
out how much cpu time it took to sort the data. You can import a library to calculate the time.
Show an example for searching a value using linear search. Table-2: Tabulate your recorded time
for the linear search and all the four sorting algorithms i.e., selection sort, insertion sort, bubble
sort and merge sort.

 Table-3: Now apply all the four sorting algorithms on the sorted data (i.e., sort the text file
according to student id / first name / last name where the text file is already sorted) and tabulate
your recorded time. Print out how much CPU time it took to sort the data.

 Table-4: Create a different text file and have 20 rows of same student details. Apply the sorting
algorithm and tabulate your readings. Print out how much CPU time it took to sort the data.

 Write a conclusion paragraph about what you understood from this lab exercise. What did you
understand from table-1, table-2, table-3 and table-4?
Annotations
"""
import random
import json
from time import process_time, perf_counter


class studentDb:
    def __init__(self):
        self.db_file_name = "student_db.json"

        self.students = []
        self.test_fnames = ['Aarav', 'Luna', 'Kai', 'Nia', 'Yusuf', 'Sakura', 'Ivan', 'Fatima', 'Jin', 'Alejandra', 'Emeka', 'Anya', 'Hiroshi', 'Ingrid', 'Kwame', 'Marta', 'Raj', 'Chen', 'Yelena', 'Diego']
        self.test_lnames = ['Kim', 'Müller', 'Singh', 'Lebedev', 'Okeke', 'Fernandez', 'Wong', 'Rossi', 'Silva', 'Kováč', 'Nguyen', 'Khan', 'Petrov', 'Díaz', 'Sato', 'Ibrahim', 'Johansson', 'Chen', 'Novak', 'Moreau']
        self.test_majors = [
                                        "Computer Science",
                                        "Mechanical Engineering",
                                        "Psychology",
                                        "Business Administration",
                                        "Biology",
                                        "Political Science",
                                        "Economics",
                                        "English Literature",
                                        "Graphic Design",
                                        "History",
                                        "Environmental Science",
                                        "Nursing",
                                        "Mathematics",
                                        "Chemical Engineering",
                                        "Sociology",
                                        "Music",
                                        "Art History",
                                        "Physics",
                                        "Philosophy",
                                        "Anthropology"
                                        ]
        self.format_student_data()

    def format_student_data(self):
        self.test_f_names = [i.lower() for i in self.test_fnames]
        self.test_l_names = [i.lower() for i in self.test_lnames]
        self.test_majors = [i.lower() for i in self.test_majors]

    def make_students(self, count = 0):
        for i in range(count-1):
            # make a student
            s = {}

            s["id"]     = int(''.join([str(random.randint(1,9)) for i in range(10)]).rstrip().lstrip())
            s["f_name"] = random.choice(self.test_f_names).lower()
            s["l_name"] = random.choice(self.test_l_names).lower()
            s["email"]  = ''.join([''.join(s["f_name"][0:2]) + ''.join(s["l_name"][0]) + ''.join([str(random.randint(0,9)) for i in range(4)]) + "@psu.edu"])
            s["major"]  = ''.join(random.choice(self.test_majors)).lower()


            self.add_student(s)

    def add_student(self, student=None):
        self.students.append(student)

    def delete_all_students(self):
        self.students = []

    def write_to_db(self):
        with open(self.db_file_name, 'w') as db:
            json.dump(self.students, db, indent=4) # indent makes it more readable

    def read_from_db(self):
        with open(self.db_file_name, 'r') as db:
            return json.load(db)

    # ------------------------ Linear Search ------------------------
    def linear_search(self, val=None, param=None):
        if not val or not param:
            return None

        for student in self.read_from_db():
            if student[param] == val:
                return student

        return None


    # ------------------------ sorting algorithms ------------------------
    def insertion_sort(self, param=None):
        if not param:
            return None

        data = self.read_from_db()

        for i in range(1, len(data)):
            key = data[i]  # value were comparing
            comp_idx = i - 1

            # shift elements until  correct spot is found
            while comp_idx >= 0 and key[param] < data[comp_idx][param]:
                data[comp_idx + 1] = data[comp_idx]
                comp_idx -= 1

            # putting the data in the right spot
            data[comp_idx + 1] = key

        return data

    def selection_sort(self, param=None):
        if not param:
            return None

        data = self.read_from_db()

        for i in range(len(data)):
            min_idx = i  # store index of current min element

            for j in range(i + 1, len(data)):
                # find the minimum of the unsorted portion
                if data[j][param] < data[min_idx][param]:
                    min_idx = j

            # Swap
            data[i], data[min_idx] = data[min_idx], data[i]

        return data

    def bubble_sort(self, param=None):
        if not param:
            return None

        data = self.read_from_db()

        for i in range(len(data)-1):
            for j in range(0, len(data) - i - 1):  # sorted part at end of list
                if data[j][param] < data[j+1][param]:
                    # swap
                    data[i], data[j] = data[j], data[i]

        return data

    # merge sort using nested functions to keep it clean
    def merge_sort(self, param=None):
        if not param:
            return None

        data = self.read_from_db()

        # merging function
        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i][param] < right[j][param]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        # dividing/entry function
        def merge_sort_recursive(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            left = merge_sort_recursive(left)
            right = merge_sort_recursive(right)

            return merge(left, right)

        sorted_data = merge_sort_recursive(data)
        return sorted_data

# print(f"Insertion: { sdb.insertion_sort(param='id') }")
# print(f"Selection: { sdb.selection_sort(param='id') }")
# print(f"Bubble: { sdb.bubble_sort(param='id') }")
# print(f"Merge: { sdb.merge_sort(param='id') }")

# ---------------------------------- Generating Stats ----------------------------------

# function to get running times
def get_run_times(f, param, count=100):
    start = perf_counter()
    for _ in range(count):
        f(param)  # assuming this resets the list to an unsorted state each time
    stop = perf_counter()

    return (stop - start) / count


sdb = studentDb()
sdb.make_students(20)
print(sdb.students)
sdb.write_to_db()

sort_stats = {k:None for k in sdb.students[0].keys()}


params = list(sdb.students[0].keys()) # getting all params except email
params.remove("email")
print(params)

funcs = {"insertion":sdb.insertion_sort, "selection":sdb.selection_sort, "bubble":sdb.bubble_sort, "merge":sdb.merge_sort}

sort_times = {
    "insertion" : {},
    "selection" : {},
    "bubble" : {},
    "merge" : {}
}

# populates sort_times with time for sorting each param
for p in params:
    for sort_algo in sort_times:
        sort_times[sort_algo][p] = get_run_times(funcs[sort_algo], param=p)

print(sort_times)


