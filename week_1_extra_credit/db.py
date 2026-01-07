from typing import List, Tuple
from course import Course
from table import display_header


def bin_search_courses(
        courses: List[Course],
        course_id: str
) -> Tuple[int, bool]:
    """ Basic binary search over a list of courses.
        Returning lower bound regardless if value exists.

        :Param vals List[Course]
        :Param value str
        :Returns Tuple[lo int, exists bool]
    """
    lo, hi = 0, len(courses)

    while lo < hi:
        mid = (lo + hi) // 2
        if courses[mid].id < course_id:
            lo = mid + 1
        else:
            hi = mid

    exists = len(courses) > lo and courses[lo].id == course_id
    return [lo, exists]


class CourseDatabase:
    """ CourseDatabase is the handle for all operations.
        It is through this class that everything is done.

        Field: course_list List[Course]
    """

    def __init__(self):
        self.course_list: List[Course] = []

    def display_specific_course(self, course_id):
        """ Searches for course by id.
            If exists call its display method, else print error.

            :Param course_id str
        """

        i, exists = bin_search_courses(self.course_list, course_id)
        if not exists:
            print("Course Does Not Exist.")
            return

        display_header()
        self.course_list[i].display()

    def display_all_courses(self):
        """ Display all courses.
            By department in alphabetical order,
            and course number in ascending order.
        """
        display_header()
        # prints by department alphabetically
        # and course number in ascending order
        for course in self.course_list:
            course.display()

    def display_dept_courses(self, dept_name):
        """ If the dept exists display its courses
            in ascending order of course number.

            :Param dept_name str
        """
        dept_name = dept_name.upper()
        display_header()
        i, _ = bin_search_courses(self.course_list, dept_name)

        list_len = len(self.course_list)

        if i < list_len:
            if self.course_list[i].department != dept_name:
                i += 1

        if i >= list_len or self.course_list[i].department != dept_name:
            print("Department Does Not Exist.")
            return

        while i < list_len and self.course_list[i].department == dept_name:
            self.course_list[i].display()
            i += 1

    def insert_course(self, course: Course):
        """ Inserts course into course_list if not exists.
            If exists print error and return

            :Param course Course
        """
        i, exists = bin_search_courses(self.course_list, course.id)
        if exists:
            print("Course already exists.")
            return

        self.course_list.insert(i, course)

    def remove_course(self, course_id: str):
        """ If course exists remove from course_list.
            else print error and return.

            :Param course_id str
        """
        i, exists = bin_search_courses(self.course_list, course_id)
        if not exists:
            print("Course does not exist.")
            return

        self.course_list.pop(i)
