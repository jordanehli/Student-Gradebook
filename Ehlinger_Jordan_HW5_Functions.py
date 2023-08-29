#Author: Jordan Ehlinger
#Assignment Number & Name: HW5 Gradebook Functions
#Due Date: N/A
#Program Description: Holds the functions to be called for HW5

#Function that can be called to ensure user is inputting a valid name
def check_valid_name():
    #intentional bad value
    name="i"
    #while loop for input validation
    while name == "i":
        try:
            name=input("Name: ")
            #ensures input isn't blank
            if name == "":
                print("Name field cannot be blank.")
                #intentional bad value
                name="i"
            #ensures input is at least 2 characters long
            elif len(name)<2:
                print("Names must be at least 2 characters long.")
                #intentional bad value
                name="i"
            #returns the valid name back to the main function
            else:
                return name
        except:
            print("That is not a valid name. Please enter again.")


#Function that can be called to ensure user is inputting a valid numeric average
def check_valid_average():
    #intentional bad value
    grade=-1
    #while loop for input validation
    while grade<0 or grade>100:
        try:
            grade=float(input("Grade: "))
            #ensures input isn't blank
            if grade == "":
                print("Grade field cannot be blank.")
                #intentional bad value
                grade=-1
            #ensures input is between 0-100 inclusive
            elif grade<0 or grade>100:
                print("Grade must be a number between 0 and 100.")
                #intentional bad value
                grade=-1
            #returns the valid grade back to the main function
            else:
                return float(grade)
        except:
            print("There is an error with your grade value. Please enter again.")
