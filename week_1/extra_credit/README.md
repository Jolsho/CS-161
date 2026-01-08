
The architecture of this project is as follows:
First, we have the most atomic class which is the `Course` class located in `course.py`.
This class offers `display()` method, which prints to std::out. 
As well as `prompt_for_fields()` which calls other methods prompting for and sanitizing user input.


The more abstract and useful to the user class is `CourseDatabase` located in `db.py`.
This is where you will find `display_specific_course()`, `display_all_courses()`, `display_dept_courses()`, `insert_course()`, and `remove_course()`.
All of these methods are self explanatory, and have comments to describe them in more depth.

For the display methods of both `Course` and inherently `CourseDatabase` there exists another module, namely `table.py`.
This is where you can find the functions `display_row`, and `display_header`.
Also in `tables.py` exists all the character limits which are also used as the widths of the tables columns.

Finally there exists `main.py` which is where the `display_menu()` function is defined, as well as the main the loop of the program.
You can see a `CourseDatabase` instance is created and then we go into a while loop which captures user input and branches based on such.
