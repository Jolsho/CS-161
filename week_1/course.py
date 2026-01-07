from table import (
    display_row,
    MIN_COURSE_NUM,
    MAX_COURSE_NUM,
    NAME_CHAR_LIMIT,
    DEPT_CHAR_LIMIT,
    DESC_CHAR_LIMIT,
    ID_CHAR_LIMIT
)


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
