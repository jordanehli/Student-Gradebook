#Author: Jordan Ehlinger
#Assignment Number & Name: HW5B Gradebook
#Due Date: N/A
#Program Description: Search a student't name and update their grade average


def main():

    import os
    import Ehlinger_Jordan_HW5_Functions

    #ask which student you would like to find
    print("To edit a student's grade search their name below.")
    name_to_find = Ehlinger_Jordan_HW5_Functions.check_valid_name()

    #open files
    data_file = open('gradebook.txt', 'r')
    temp_file = open('temp.txt', 'w')

    #see if search was found
    name_found = False

    name = data_file.readline().rstrip('\n')

    while name != '':

        #strip the newline fr
        grade = data_file.readline().rstrip('\n')

        #print student name to file
        temp_file.write(name + '\n')

        #see if this is the desired value and either print or update as needed
        if name == name_to_find:
            new_grade = Ehlinger_Jordan_HW5_Functions.check_valid_average()
            #write new grade
            temp_file.write(str(new_grade) + '\n')
            
            #set flag that name was found
            name_found = True

        else:
            temp_file.write(grade + '\n')

        #read in next line (if there is one)
        name = data_file.readline().rstrip('\n')

    #clean up files
    #close both files
    data_file.close()
    temp_file.close()

    #delete the original file
    os.remove('gradebook.txt')

    #rename the temp file
    os.rename('temp.txt', 'gradebook.txt')

    #let user know if match was found
    if name_found == True:
        print('The gradebook has been updated!')
    else:
        print('The student was not found')

#Call the main function.
main()
