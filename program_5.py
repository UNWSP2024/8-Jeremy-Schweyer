# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."
# Then ask the user for a subject (like "COS").
# Finally, the program will display the ID and name of all the courses having that subject.


def add(course_catalog):
    course_id = input("Enter Course ID: ")
    course_name = input("Enter Course Name: ")


    if course_id not in course_catalog:
        course_catalog[course_id] = course_name


course_catalog = {}


keep_adding = 'y'
while keep_adding == 'y':
    add(course_catalog)
    keep_adding = input("Would you like to add another course? (y/n): ")

search_subject = input("Enter a subject to search for: ")
for course_id, course_name in course_catalog.items():
    if search_subject in course_id:
        print("Your course is: ", course_id, course_catalog[course_id])
    else:
        print("Your subject is not found")
