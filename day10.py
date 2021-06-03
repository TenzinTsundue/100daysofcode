#function with output
"""
def format_name(f_name, l_name):
  ff_name = f_name.title()
  fl_name = l_name.title()
  return f"{ff_name} {fl_name}" 

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

name = format_name(f_name, l_name)

print(f"Formated name is {name}")
"""

#function with multiple return
"""
def format_name(f_name, l_name):
  if f_name=="" or l_name=="":
    return "You did't provide valid input"     #early return
  ff_name = f_name.title()
  fl_name = l_name.title()
  return f"Result: {ff_name} {fl_name}"        #result return

print(format_name(input("Your first name: "), input("Your last name: ")))
"""

#Check how many days in a month of year
"""
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month(year, month):
  if (year % 4) == 0:
     if (year % 100) == 0:
         if (year % 400) == 0:
          leap_year = True
         else:
          leap_year =False
     else:
      leap_year = True
  else:
    leap_year = False

  if leap_year==True :
    return 29
  else:
    return month_day[month]

print(f'Result: {days_in_month(int(input("Enter year? ")), int(input("Enter month? ")))}')
"""

#Docstring

#Calulator

ascii_art = """
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |      __      | || |   _____      | || |     ______   | |
| |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'
 """


print(ascii_art)

def evaluate(f_number, operator, s_number):
  concat = f_number+operator+s_number
  return eval(concat)

print(evaluate(input("Enter first no? "),input("Enter operator? "), input("Enter second no? ")))





