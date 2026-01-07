from typing import List, Tuple

column_names = [
    "Department",
    "Number",
    "Name",
    "Credits",
    "Description"
]

NAME_CHAR_LIMIT = 30

# "MTH 123" == 7
ID_CHAR_LIMIT = 7
MIN_COURSE_NUM = 101
MAX_COURSE_NUM = 499

DEPT_CHAR_LIMIT = 3
DESC_CHAR_LIMIT = 100
MAX_CREDITS = 6

# len of title "Credits" longer than 0 -> 6
CREDITS_CHAR_LIMIT = len(column_names[3])

widths = [
    DEPT_CHAR_LIMIT,
    ID_CHAR_LIMIT,
    NAME_CHAR_LIMIT,
    CREDITS_CHAR_LIMIT,
    DESC_CHAR_LIMIT
]


def display_row(fields: List[str]):
    """ Given a List[str] zip each field with its corresponding.
        column width in 'widths' list.
        Pass the zipped values into a formated string to display them.
    """
    print(" ".join(f"{str(v):<{w}.{w}}" for v, w in zip(fields, widths)))


def display_header():
    """ Displays column_name(header_names) via display_row(). """
    display_row(column_names)


class Course:
    """ Course is the most atomic data structure.
        Essentially just acts a convenient way to access
        attributes of a course in the database.
        As well as seperate logic of building a course
        into an object.

        Field: id: str
        Field: name: str
        Field: credits: int
        Field: department: str
        Field: description: str
    """

    def __init__(self,
                 id="",
                 name="",
                 credits=0,
                 department="",
                 description=""):
        self.id = id
        self.name = name
        self.credits = credits
        self.department = department
        self.description = description

    def display(self):
        """ Passes fields = [dept, id, name, credits, description]
            to display_row().
        """
        number = self.id.split()[1] if len(self.id.split()) > 1 else ""
        fields = [
            self.department,
            number,
            self.name,
            self.credits,
            self.description
        ]
        display_row(fields)

    def prompt_for_fields(self):
        """ Guides user to create a course.
            Input is sanitized at each step to ensure consistency and safety.
            It is single pass with no exits.
            Meaning you can't go back and must finish creating it.
            Not ideal, but works for now.
        """
        self.input_course_id()
        self.input_course_name()
        self.input_course_description()
        self.input_course_credits()

    def input_course_id(self):
        while True:
            course_id = input("Enter Course Id(ex. MTH 123): ").split()

            if len(course_id) < 2:
                print("Course Id = <Department> <Number>")
                continue
            try:
                int_num = int(course_id[1])
                if int_num < MIN_COURSE_NUM or int_num > MAX_COURSE_NUM:
                    print(
                        "Number must be" +
                        f" {MIN_COURSE_NUM} <= course_num <= {MAX_COURSE_NUM}."
                    )
                    continue
            except (IndexError, ValueError):
                print("Malformed number input.")
                continue

            department = course_id[0]
            number = course_id[1]

            if len(department) > DEPT_CHAR_LIMIT:
                print(f"Department symbol must be {DEPT_CHAR_LIMIT} chars.")

            elif len(course_id) > ID_CHAR_LIMIT:
                print(
                    "Full Course Number must be less than" +
                    f" {ID_CHAR_LIMIT} chars."""
                )
            else:
                self.department = department.upper()
                self.id = f"{self.department} {number}"
                break

    def input_course_name(self):
        while True:
            name_in = input("Enter Course Name: ")
            if len(name_in) >= NAME_CHAR_LIMIT:
                print(name_in, len(name_in))
                print(f"Name must be less than {NAME_CHAR_LIMIT} chars.")
            else:
                self.name = name_in
                break

    def input_course_description(self):
        while True:
            desc_in = input("Enter Course Description: ")
            if len(desc_in) >= DESC_CHAR_LIMIT:
                # I dont normally do this, but there is a char/line limit
                print(f'''
                    Description must be less than {DESC_CHAR_LIMIT} chars.
                ''')
            else:
                self.description = desc_in
                break

    def input_course_credits(self):
        while True:
            creds = input("Enter total course credits: ").split()[0]
            try:
                self.credits = int(creds)
                if self.credits < 0 or self.credits > 6:
                    print("Credits must be >= 0 and <= 6.")
                else:
                    break
            except (IndexError, ValueError):
                print("Malformed number input.")


def bin_search_courses(
        courses: List[Course],
        course_id: str
) -> Tuple[int, bool]:
    """ Basic binary search over a list of courses.
        Looking for value at course.id for elements of vals.
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

        Field: course_lid List[Course]
            all courses sorted by id
    """

    def __init__(self):
        self.course_list: List[Course] = []

    def display_specific_course(self, course_id):
        """ Searches for course by id.
            If exists call its display method,
            else print error.

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
            First by department in alphabetical order,
            then by course number in ascending order.
        """
        display_header()
        # prints by department alphabetically
        # and course number in ascending order
        for course in self.course_list:
            course.display()

    def display_dept_courses(self, dept_name=""):
        """ If the dept exists display its courses
            in ascending order of course number.

            :Param dept_name str default=""
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
        """ Inserts course in course_list if not exists.
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

            :Param course_id str
        """
        i, exists = bin_search_courses(self.course_list, course_id)
        if not exists:
            print("Course does not exist.")
            return

        self.course_list.pop(i)


def display_menu():
    """ Displays all options for the user.
        No Params, just pushing to std::out.
    """
    print("     Welcome To COCC Course Database!    ")
    print("==============================================")
    print("Enter 'insert' and follow the prompt to add a course.")
    print("Enter 'remove <course_number>' to delete a course.")
    print("Enter 'view <dept_name> <course_number>' to see a specific course.")
    print("Enter 'all' to see every course in the databse.")
    print("Enter 'dept <dept_symbol>' to see every course in a department.")
    print("Enter 'help' to see this menu again.")
    print("Enter 'exit' to exit the program.")


db = CourseDatabase()


display_menu()

# Main loop
while True:
    """This is just a simple while loop which prompts users.
        User inputs, this branches based on input.
    """

    print("")
    command = input("Enter command: ").strip()
    print("")

    if command == "insert":
        course = Course()
        course.prompt_for_fields()
        db.insert_course(course)

    elif command.startswith("remove "):
        split = command.split()
        if len(split) < 3:
            print("invalid command")
            continue

        course_id = f"{split[1].upper()} {split[2]}"

        db.remove_course(course_id)

    elif command.startswith("view "):
        split = command.split()
        if len(split) < 3:
            print("invalid command")
            continue

        course_id = f"{split[1].upper()} {split[2]}"
        db.display_specific_course(course_id)

    elif command == "all":
        db.display_all_courses()

    elif command.startswith("dept "):
        split = command.split(" ", 1)
        if len(split) < 2:
            print("invalid command")
            continue

        db.display_dept_courses(split[1].upper())

    elif command == "exit":
        print("Goodbye!")
        break

    elif command == "help":
        display_menu()

    else:
        print("Unknown command.")
