"""
Request name from the user using input()
Request age from the user 
Request House number from the user
Request Street name from the user 

Print out single sentence containing name, age, house, and street name from user 
This is (name). They are (age) years old and live at house number (house number) on (street name). 
"""

name = input("Enter your name: ")
age = input("Enter your age: ")
house_number = input("Enter your house number: ")
street_name = input("Enter your street name: ")

print("This is {}. They are {} years old and live at house number {} on {}.".format(name,age,house_number,street_name))
