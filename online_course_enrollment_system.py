print("Welcome to Online Course Enrollment")

students_enrolled = {
  "JAVASCRIPT": set(),
  "PYTHON": set(),
  "JAVA": set(),
  "HTML": set(),
  "PHP": set(),
  "CSS": set()
}

menu = {
  "ENROLL": "Enroll to a course",
  "DROP": "Drop from a course",
  "VIEW": "View all students enrolled",
  "OVERLAPS": "View common names enrolled",
  "DIFFERENCE": "View difference",
  "EXIT": "Exit program"
}

def show_course(students_enrolled):
  print("\n------COURSES------")
  for course in students_enrolled:
    print(course)
  print("-------------------")
  
def show_menu(menu):
  print("\n---------------MENU---------------")
  for feature, description in menu.items():
    print(f"{feature}: {description}")
  print("----------------------------------")
      
def view_students_enrolled():
  print("\n---------STUDENTS ENROLLED---------")
  for course, name in students_enrolled.items():
    if name:
      print(f"{course}: {name}")
    else:
      print(f"{course}: No students enrolled.")
  print("-----------------------------------")
  
def ask_for_course(prompt):
  course = input(prompt).strip().upper() 
  
  if not course:
    print("\nPlease enter a course.")
    return None
  
  if course not in students_enrolled:
    print("\nPlease enter a valid course.")
    return None
  return course
  
def run_program():
  while True:
    show_menu(menu)
    
    ask_feature = input("\nWhat would you like to do: ").strip().upper()
    
    if not ask_feature:
      print("\nPlease enter a valid option.")
      continue
    
    if ask_feature == "ENROLL":
      show_course(students_enrolled)
      
      get_course = ask_for_course("\nChoose course to enroll: ")
      
      if get_course is None:
        continue
      
      course_set = students_enrolled[get_course]
      
      name = input("\nEnter your name: ").strip().title()
        
      if not name:
        print("\nPlease enter your name.")
        continue
  
      course_set.add(name)
        
      print("\nYou have enrolled successfully!")
      
      proceed = input("\nPress Enter to continue...")
          
    elif ask_feature == "DROP":
      get_course = ask_for_course("\nChoose course to drop: ")
      
      if get_course is None:
        continue
      
      course_set = students_enrolled[get_course]
      
      remove_name = input("\nEnter your name: ").strip().title()
        
      if not remove_name:
        print("\nPlease enter your name.")
        continue
        
      if remove_name in course_set:
        confirm = input(f"\nAre you sure you want to drop the course {get_course} (y/n): ").strip().lower()
        
        if confirm == "y":
          course_set.remove(remove_name)
        else:
          print("\nDropping cancelled!")
          continue
      else:
        print("\nName doesn't exist.")
        continue
        
      print("\nDrop successfully, See ya!")
      
      proceed = input("\nPress Enter to continue...")
  
    elif ask_feature == "VIEW":
      view_students_enrolled()
      
      proceed = input("\nPress Enter to continue...")
      
    elif ask_feature == "OVERLAPS":
      first_course = ask_for_course("\nEnter the first course: ")
      
      if first_course is None:
        continue
      
      first = students_enrolled[first_course]
      
      second_course = ask_for_course("\nEnter the second course: ")
      
      if second_course is None:
        continue
      
      if second_course == first_course:
        print("\nPlease enter a different course.")
        continue
      
      second = students_enrolled[second_course]
      
      common = first.intersection(second)
      
      if not common:
        print("\nNo common names.")
        continue
      
      print(f"\nCommon names for the course {first_course} and {second_course}:")
      print(f"\n{common}")
      
      proceed = input("\nPress Enter to continue...")
      
    elif ask_feature == "DIFFERENCE":
      first_course = ask_for_course("\nEnter the first course: ")
      
      if first_course is None:
        continue
      
      first = students_enrolled[first_course]
      
      second_course = ask_for_course("\nEnter the second course: ")
      
      if second_course is None:
        continue
      
      if second_course == first_course:
        print("\nPlease enter a different course.")
        continue
      
      second = students_enrolled[second_course]
      
      print(f"\nThe student/s enrolled in {first_course} but not in the {second_course} course:")
      print(f"\n{first.difference(second)}")
      
      proceed = input("\nPress Enter to continue...")
      
    elif ask_feature == "EXIT":
      print("\nGoodbye!")
      break
      
    else:
      print("\nPlease enter a valid choice.")
      
run_program()