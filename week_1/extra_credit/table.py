from typing import List

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
