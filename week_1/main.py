from db import CourseDatabase
from course import Course


def display_menu():
    """ Displays all options for the user.
        No Params, just pushing to std::out.
    """
    print("     Welcome To COCC Course Database!    ")
    print("==============================================")
    print("Enter 'insert' and follow the prompt to add a course.")
    print("Enter 'remove <course_number>' to delete a course.")
    print("Enter 'view <dept_symbol> <course_number>' to see a course.")
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
