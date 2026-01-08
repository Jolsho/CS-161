from db import CourseDatabase
from course import Course


def display_menu():
    """ Displays all options for the user.
        No Params, just pushing to std::out.
    """
    print("     Welcome To COCC Course Database!    ")
    print("==============================================")
    print("Enter 'insert' and follow the prompt to add a course.")
    print("Enter 'remove <dept_symbol> <course_number>' to delete a course.")
    print("Enter 'view <dept_symbol> <course_number>' to see a course.")
    print("Enter 'all' to see every course in the databse.")
    print("Enter 'dept <dept_symbol>' to see every course in a department.")
    print("Enter 'help' to see this menu again.")
    print("Enter 'exit' to exit the program.")


db = CourseDatabase()


display_menu()

CMD_IDX = 0

# Main loop
while True:
    """This is just a simple while loop which prompts users.
        User inputs, this branches based on input.
    """

    print("")
    command = input("Enter command: ").strip().split()
    print("")
    if len(command) == 0:
        print("Need a command.")
        continue

    if command[CMD_IDX] == "insert":
        course = Course()
        course.prompt_for_fields()
        db.insert_course(course)

    elif command[CMD_IDX] == "remove":
        if len(command) < 3:
            print("invalid command")
            print("    try 'remove <dept_symbol> <course_number>")
            continue

        course_id = f"{command[CMD_IDX + 1].upper()} {command[CMD_IDX + 2]}"
        db.remove_course(course_id)

    elif command[CMD_IDX] == "view":
        if len(command) < 3:
            print("invalid command")
            print("    try 'view <dept_symbol> <course_number>")
            continue

        course_id = f"{command[CMD_IDX + 1].upper()} {command[CMD_IDX + 2]}"
        db.display_specific_course(course_id)

    elif command[CMD_IDX] == "all":
        db.display_all_courses()

    elif command[CMD_IDX] == "dept":
        if len(command) < 2:
            print("invalid command")
            print("    try 'dept <dept_symbol>")
            continue

        db.display_dept_courses(command[CMD_IDX + 1].upper())

    elif command[CMD_IDX] == "exit":
        print("Goodbye!")
        break

    elif command[CMD_IDX] == "help":
        display_menu()

    else:
        print("Unknown command.")
